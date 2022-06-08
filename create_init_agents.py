'''
CREATE_INIT_AGENTS
*****
the create agents function will call the required functions to
generate the genome, brain, and traits for each agent, then
return the agents to the main function to do run
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


import random                                                       # import functions to generate the agent
from create_init_genome import GenerateGenome
from create_init_brain import GenerateBrain
from create_init_traits import GenerateTraits


def CreateAgent(config, agents, score):                             # main function to generate a list of agents

    Agents = []
    new_agents = []

    for i in range(config['population']):                           # main loop to generate the 4 parts of an agent

        new_agent = []                                              # agent data structure is:
                                                                    # if x is the agents index number (order they were created)
        name = random.randrange(1000,9999)                                  # agent[x][0] AGENT NAME
        new_agent.append(name)                                              # agent[x][1] GENOME
                                                                            # agent[x][2] BRAIN
        genome = GenerateGenome(config)                                     # agent[x][3] TRAITS
        new_agent.append(genome)

        brain = GenerateBrain(genome, config)
        new_agent.append(brain)

        traits = GenerateTraits(genome, config)
        new_agent.append(traits)

        Agents.append(new_agent)

    return Agents
