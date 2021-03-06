'''
ENVIRONMENT
*****
Define and initialise the environment the agents will
interact in.
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


import numpy as np
import random


def RandomizeFood(size, abundance):                                 # Determine random locations for the food on map

    offset_x = 0
    offset_y = 0
    location_x = []
    location_y = []

    for i in range(round(size/100)):

        for a in range(round(size/100)):

            for b in range(abundance):

                location_x.append(random.randrange(0,100) + (a * 100))
                location_y.append(random.randrange(0,100) + (i * 100))
    return location_x, location_y


def AddFood(map, x, y):                                             # Add food to the map

    if len(x) == len(y):

        for i in range(len(x)):

            map[x[i]][y[i]] = 50

    return map


def RandomiseAgents(config):                                        # Determine random locations for each agent

    x = []
    y = []
    metadata = []

    for i in range(config['population']):

        x.append(random.randrange(0, config['environment_size']))
        y.append(random.randrange(0, config['environment_size']))

    metadata.append(x)
    metadata.append(y)

    return metadata


def AddAgents(environment, metadata):                               # Add Agents to the map

    if len(metadata[0]) == len(metadata[1]):

        for i in range(len(metadata[0])):

            environment[metadata[0][i]][metadata[1][i]] = 250

    return environment


def CreateEnvironment(agents, config):                              # main function to create empty numpy array and
                                                                    # add food and agents
    size = int(config['environment_size'])
    abundance = int(config['food_abundance'])

    init_map = np.zeros((size, size))
    food_x, food_y = RandomizeFood(size, abundance)
    init_map = AddFood(init_map, food_x, food_y)
    metadata = RandomiseAgents(config)
    environment = AddAgents(init_map, metadata)

    return metadata, environment
