'''
AGENT - Main
*****
The main function excecutes the program and stores the configuration
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''



from create_init_agents import CreateAgent                          # Import other functions for excecution
from environment import CreateEnvironment
from do_run import DoRun
from evolve import Evolve


config =            {'steps': 500,                                  # how many timesteps per generation
                    'population': 70,                               # how many agents per generation
                    'network_genes': 10,                            # how many unique network genes per agent
                                                                    # (default is 2 unique genes, of which one is mutated)
                    'trait_genes': 1,                               # how many unique trait genes per agent
                                                                    # (default is 2 unique genes, of which one is mutated,
                                                                    # and the mutated gene is currently always dominant)
                    'traits': 1,                                    # how many different traits the agents have
                    'input_neurons': 4,                             # how many input neurons an agent has
                    'hidden_neurons': 1,                            # how many hidden neurons an agent has
                    'output_neurons': 4,                            # how many output neurons an agent has
                    'environment_size': 700,                        # size of square environment (must be multiple of 100)
                    'food_abundance': 15,                           # how many food items spawn in a 100x100 area
                    'sight_range': 50,                              # how many blocks in each cardinal an agent can see
                    'generations': 50000,                           # how many evolution generations per run
                    'score_display_rate': 5}                        # how many generations per add of score to printed tally


def Main():                                                         # Main function to execute all functions for run

    Agents = []
    Score = 0
    tally = []
    Agents = CreateAgent(config, Agents, Score)                     # calls CreateAgent from create_init_agents

    for i in range(config['generations']):                          # main loop calls 3 functions to run program,
                                                                    # CreateEnvironment, DoRun, and Evolve.
        print(f"\n\n========GENERATION {i}========")                # the score is also appened to the tally

        Metadata, Environment = CreateEnvironment(Agents, config)
        Metadata, Environment, Score= DoRun(Agents, Environment, config, Metadata, i)
        Agents = Evolve(Agents, Score, config)

        if i % config['score_display_rate'] == 0:
            tally.append(Score)


    print(f"\n\n========COMPLETE========")                          # print scores
    print("Final Scores per 5 generations=\n")

    for i in range(len(tally)):

        print(f'Gen {i*5} scores = {tally[i]}')



Main()
