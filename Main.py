from create_init_agents import CreateAgent
from environment import CreateEnvironment
from do_run import DoRun
from evolve import Evolve


config =    {'steps': 500,
                    'population': 70,
                    'network_genes': 10,
                    'trait_genes': 1,
                    'traits': 1,
                    'input_neurons': 4,
                    'hidden_neurons': 1,
                    'output_neurons': 4,
                    'environment_size': 700,
                    'food_abundance': 15,
                    'sight_range': 50,
                    'generations': 50000}


def Main():
    Agents = []
    Score = 0
    tally = []
    Agents = CreateAgent(config, Agents, Score)

    for i in range(config['generations']):

        print(f"\n\n========GENERATION {i}========")

        Metadata, Environment = CreateEnvironment(Agents, config)

        Metadata, Environment, Score= DoRun(Agents, Environment, config, Metadata, i)

        Agents = Evolve(Agents, Score, config)




        if i % 5 == 0:
            tally.append(Score)


    print(f"\n\n========COMPLETE========")
    print("Final Scores per 5 generations=\n")
    for i in range(len(tally)):
        print(f'Gen {i*5} scores = {tally[i]}')

Main()
