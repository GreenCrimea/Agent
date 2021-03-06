'''
DO_RUN
*****
the function will loop for every step and calculate the
actions of the agents
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


import random
from calculate_action import CalculateAction


def UpdateMap(agents, environment, config, metadata, score):        # Call the CalculateAgent function for each agent

    for i in range(config['population']):

        metadata, environment, score = CalculateAction(agents, environment, config, metadata, i, score)

    return metadata, environment, score


def DoRun(agents, environment, config, metadata, z):                # Call the UpdateMap function for each step

    score = []
    a = 0

    for i in range(len(agents)):

        score.append(a)

    steps = config['steps']

    for i in range(steps):

        print(f'GEN{z}, STEP{i}___agent 0>{metadata[0][0]}, {metadata[1][0]} | agent 1>{metadata[0][1]}, {metadata[1][1]} | agent 2>{metadata[0][2]}, {metadata[1][2]}')

        metadata, environment, score = UpdateMap(agents, environment, config, metadata, score)

    return metadata, environment, score
