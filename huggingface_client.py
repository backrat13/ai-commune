"""
Hugging Face LLM Client for AI Commune
Provides completely free, open-source LLM inference using Hugging Face Transformers.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from typing import List, Optional, Dict, Any
from loguru import logger


class HuggingFaceClient:
    """Free, open-source LLM client using Hugging Face Transformers."""

    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        """Initialize Hugging Face client.

        Args:
            model_name: Hugging Face model to use (default: DialoGPT-medium)
        """
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        logger.info(f"🚀 Initializing Hugging Face model: {model_name} on {self.device}")

        try:
            # Initialize tokenizer and model
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            self.model.to(self.device)
            self.model.eval()

            # Create pipeline for easier generation
            self.generator = pipeline(
                'text-generation',
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if self.device == "cuda" else -1
            )

            logger.success(f"✅ Model {model_name} loaded successfully")

        except Exception as e:
            logger.error(f"❌ Failed to load model {model_name}: {e}")
            logger.info("🔄 Falling back to smaller model...")
            # Fallback to a smaller model if the primary fails
            self._fallback_init()

    def _fallback_init(self):
        """Fallback initialization with a smaller model."""
        fallback_models = ["distilgpt2", "gpt2"]

        for model_name in fallback_models:
            try:
                logger.info(f"🔄 Trying fallback model: {model_name}")
                self.tokenizer = AutoTokenizer.from_pretrained(model_name)
                if self.tokenizer.pad_token is None:
                    self.tokenizer.pad_token = self.tokenizer.eos_token

                self.model = AutoModelForCausalLM.from_pretrained(model_name)
                self.model.to(self.device)
                self.model.eval()

                self.generator = pipeline(
                    'text-generation',
                    model=self.model,
                    tokenizer=self.tokenizer,
                    device=0 if self.device == "cuda" else -1
                )

                self.model_name = model_name
                logger.success(f"✅ Fallback model {model_name} loaded successfully")
                return

            except Exception as e:
                logger.warning(f"⚠️  Fallback model {model_name} also failed: {e}")
                continue

        logger.error("❌ All models failed to load. Please check your internet connection and disk space.")
        raise RuntimeError("Failed to load any model")

    def list_models(self) -> List[str]:
        """List available models (for compatibility).

        Returns:
            List of available model names
        """
        return [self.model_name]

    def generate(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 150) -> str:
        """Generate response using the loaded model.

        Args:
            prompt: The prompt to send to the model
            system_prompt: Optional system prompt (will be combined)
            temperature: Sampling temperature (0.0-2.0)
            max_tokens: Maximum tokens to generate

        Returns:
            Generated response text
        """
        try:
            # Combine system prompt and user prompt
            full_prompt = prompt
            if system_prompt:
                full_prompt = f"{system_prompt}\n\n{prompt}"

            # Generate response
            with torch.no_grad():
                inputs = self.tokenizer(
                    full_prompt,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=512
                )
                inputs = {k: v.to(self.device) for k, v in inputs.items()}

                outputs = self.model.generate(
                    **inputs,
                    max_length=min(inputs['input_ids'].shape[1] + max_tokens, 512),
                    temperature=max(0.1, min(2.0, temperature)),
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    num_return_sequences=1
                )

            # Decode and clean response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Remove the original prompt from response if present
            if response.startswith(full_prompt):
                response = response[len(full_prompt):].strip()

            return response.strip()

        except Exception as e:
            logger.error(f"❌ Generation failed: {e}")
            return f"I apologize, but I encountered an error while processing your request. Error: {str(e)[:100]}"

    def __str__(self) -> str:
        """String representation of the client."""
        return f"HuggingFaceClient(model='{self.model_name}', device='{self.device}')"
