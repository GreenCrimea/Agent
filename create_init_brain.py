'''
CREATE_INIT_BRAIN
*****
the create brain function extracts the network parameters
from the agents genome and creates a list of network neurons
and connections
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


import math


def CheckNetworkGene(gene):                                         # Check if a gene is encoding network infomation

    if int(gene[0], 16) <= 7:

        return True

    else:

        return False


def ExtractGeneInfoDecimal_a(gene, index):                          # Converts the individual gene bits into decimal

    return int(gene[index], 16)

Ext_Dec_a = ExtractGeneInfoDecimal_a


def ExtractGeneInfoDecimal(gene, index):                            # converts the individual gene bits into decimal
                                                                    # and add one so theres no multiply by 0
    return int(gene[index], 16) + 1

Ext_Dec = ExtractGeneInfoDecimal_a


def GenerateBrain(genome,config):

    brain = []

    for i in range(len(genome)):                                    # main loop for creating the brain structure.

        input_neuron = 0                                            # for each gene the gene type is determined, then
        output_neuron = 0                                           # the neuron numbers it encodes are decoded and
        output_neuron2 = 0                                          # multiplied by the multiplier. then the weights are
        hidden_neuron = 0                                           # determined, and the single structure is appended
        hidden_neuron2 = 0                                          # to the brain
        input_output_weight = 0
        input_hidden_weight = 0
        hidden_hidden_weight = 0                        # for the massive if chain:
        hidden_output_weight = 0                        # IF GENE_TYPE:
        output_output_weight = 0                        # NEURON = (ENCODED_NEURON * MULTIPLIER) % NEURON_NUMBER
                                                        # WEIGHT = ((NEURON_1 * NEURON_2) * MULTIPLIER) * ENCODED WEIGHT
        if CheckNetworkGene(genome[i]):

            if Ext_Dec_a(genome[i], 0) == 0:

                input_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                input_output_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 2)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 4)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 1:

                input_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_neuron = round((Ext_Dec(genome[i], 4) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                input_hidden_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 5)) / 6553.6), 4)
                hidden_output_weight = round((((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 6)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 2:

                input_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_neuron = round((Ext_Dec(genome[i], 4) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                input_hidden_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 5)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 3:

                hidden_neuron = round((Ext_Dec(genome[i], 4) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_output_weight = round((((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 6)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 4:

                output_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron2 = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_output_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 2)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 4)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 5:

                input_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_neuron = round((Ext_Dec(genome[i], 4) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                input_hidden_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 5)) / 6553.6), 4)
                input_output_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 2)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 4)) / 6553.6), 4)

            if Ext_Dec_a(genome[i], 0) == 6:

                input_neuron = round((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                output_neuron = round((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_neuron = round((Ext_Dec(genome[i], 4) * Ext_Dec(genome[i], 7)) % config['input_neurons'])
                hidden_output_weight = round((((Ext_Dec(genome[i], 2) * Ext_Dec(genome[i], 4)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 6)) / 6553.6), 4)
                input_output_weight = round((((Ext_Dec(genome[i], 1) * Ext_Dec(genome[i], 2)) * Ext_Dec(genome[i], 7) * Ext_Dec(genome[i], 4)) / 6553.6), 4)


            structure = []
            structure.append(Ext_Dec(genome[i], 0))
            structure.append(input_neuron)
            structure.append(output_neuron)
            structure.append(output_neuron2)
            structure.append(hidden_neuron)
            structure.append(hidden_neuron2)
            structure.append(input_output_weight)
            structure.append(input_hidden_weight)
            structure.append(hidden_hidden_weight)
            structure.append(hidden_output_weight)
            structure.append(output_output_weight)
            brain.append(structure)

    brain = tuple(brain)

    return brain
