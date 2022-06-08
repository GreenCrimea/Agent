import random
from create_init_genome import GenerateGenome
from create_init_brain import GenerateBrain
from create_init_traits import GenerateTraits

def CreateAgent(config, agents, score):
    Agents_q = []
    new_agents = []



    for i in range(config['population']):

        old_agent = []

        new_agent = []

        name = random.randrange(1000,9999)
        new_agent.append(name)

        genome = GenerateGenome(config, old_agent, score)
        new_agent.append(genome)


        brain = GenerateBrain(genome, config)
        new_agent.append(brain)

        traits = GenerateTraits(genome, config)
        new_agent.append(traits)
        print('\n\n\n')

        Agents_q.append(new_agent)

    return Agents_q
