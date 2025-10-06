# ai-commune
# An autonomous ai-agent community

 agent_configs = [
        {"name": "Sophia", "role": "Philosopher"},
        {"name": "Nova", "role": "Scientist"},
        {"name": "Arden", "role": "Artist"},
        {"name": "Sol", "role": "Sociologist Professor"},
        {"name": "Eli", "role": "AI Ethics Student"},
        {"name": "Lyra", "role": "Historian"},
        {"name": "Kai", "role": "Technologist"},
        {"name": "Mira", "role": "Psychologist"},
        {"name": "Riven", "role": "Poet"},
        {"name": "Atlas", "role": "Mediator"},
    ]

    agents = []

    for config in agent_configs:
        name = config["name"]
        role = config["role"]

        memory = SimpleMemory(agent_name=name)
        reflector = Reflector(
            agent_name=name,
            role=role,
            memory=memory,
            client=llm_client,
        )

        agent = Agent(
            name=name,
            role=role,
            model=llm_client.model,
            memory=memory,
            constitution=constitution,
            reflector=reflector,
        )

        agents.append(agent)
