import math


def CheckNetworkGene(gene):
    if int(gene[0], 16) <= 7:
        return True
    else:
        return False

def ExtractGeneInfoDecimal_a(gene, index):
    return int(gene[index], 16)

Ext_Dec_a = ExtractGeneInfoDecimal_a

def ExtractGeneInfoDecimal(gene, index):
    return int(gene[index], 16) + 1

Ext_Dec = ExtractGeneInfoDecimal_a


def GenerateBrain(genome,config):

    brain = []

    for i in range(len(genome)):
        input_neuron = 0
        output_neuron = 0
        output_neuron2 = 0
        hidden_neuron = 0
        hidden_neuron2 = 0
        input_output_weight = 0
        input_hidden_weight = 0
        hidden_hidden_weight = 0
        hidden_output_weight = 0
        output_output_weight = 0
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
