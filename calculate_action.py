

def CalculateInputLayer(environment, config, metadata, num):

    neuron0 = 0
    neuron1 = 0
    neuron2 = 0
    neuron3 = 0

    for i in range(config['sight_range']):
        try:
            x = environment[(metadata[0][num] + (i + 1))][metadata[1][num]]
            if x == 50:
                neuron0 = (i+1) * 2
                break
            elif x == 250:
                neuron0 = -((i+1) * 2)
                break
            else:
                neuron0 = 0
        except IndexError:
            break

    for i in range(config['sight_range']):
        try:
            y = environment[metadata[0][num]][(metadata[1][num] + (i + 1))]
            if y == 50:
                neuron1 = (i+1) * 2
                break
            elif y == 250:
                neuron1 = -((i+1) * 2)
                break
            else:
                neuron1 = 0
        except IndexError:
            break

    for i in range(config['sight_range']):
        try:
            x = environment[(metadata[0][num] - (i + 1))][metadata[1][num]]
            if x == 50:
                neuron2= (i+1) * 2
                break
            elif x == 250:
                neuron2 = -((i+1) * 2)
                break
            else:
                neuron2 = 0
        except IndexError:
            break

    for i in range(config['sight_range']):
        try:
            y = environment[metadata[0][num]][(metadata[1][num] - (i + 1))]
            if x== 50:
                neuron3 = (i+1) * 2
                break
            elif x == 250:
                neuron3 = -((i+1) * 2)
                break
            else:
                neuron3 = 0
        except IndexError:
            break

    input_layer = []
    input_layer.append(neuron0)
    input_layer.append(neuron1)
    input_layer.append(neuron2)
    input_layer.append(neuron3)
    return input_layer




def CalculateOutputLayer(agent, network, num):


    for i in range(len(agent[num][2])):





        if agent[num][2][i][0] == 0:
            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[0][agent[num][2][i][1]] + 0.1)* (agent[num][2][i][6] + agent[num][3][0]['risk_taking'])) / 10

        if agent[num][2][i][0] == 1:
            network[1][0] = network[1][0] + ((network[0][agent[num][2][i][1]] + 0.1)* (agent[num][2][i][7] + agent[num][3][0]['risk_taking'])) /10

            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[1][0] +0.1)* (agent[num][2][i][9] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 2:
            network[1][0] = network[1][0] + ((network[0][agent[num][2][i][1]] +0.1)* (agent[num][2][i][7] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 3:
            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[0][1] +0.1)* (agent[num][2][i][9] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 4:
            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[2][agent[num][2][i][3]]+0.1) * (agent[num][2][i][10] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 5:
            network[1][0] = network[1][0] + ((network[0][agent[num][2][i][1]] +0.1)* (agent[num][2][i][7] + agent[num][3][0]['risk_taking'])) /10

            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[0][agent[num][2][i][1]]+0.1) * (agent[num][2][i][6] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 6:
            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[1][0] + 0.1)* (agent[num][2][i][9] + agent[num][3][0]['risk_taking'])) /10

            network[2][agent[num][2][i][2]] = network[2][agent[num][2][i][2]] + ((network[0][agent[num][2][i][1]] + 0.1)* (agent[num][2][i][6] + agent[num][3][0]['risk_taking'])) /10

        if agent[num][2][i][0] == 7:
            network[2][agent[num][2][i][4]] = network[2][agent[num][2][i][4]] + ((network[2][agent[num][2][i][5]] +0.1) * (agent[num][2][i][8] + agent[num][3][0]['risk_taking'])) /10

    return network


def CalculateMovement(agent, network, metadata, environment, num, score):

    network2 = network[2]
    direction = 0
    network_sorted = max(network2)


    for i in range(len(network[2])):
        if network[2][i] == network_sorted:
            direction = i

    if direction == 0:
        try:
            if environment[(metadata[0][num] + 1)][metadata[1][num]] == 0:
                environment[(metadata[0][num] + 1)][metadata[1][num]] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[0][num] = metadata[0][num] + 1
            elif environment[(metadata[0][num] + 1)][metadata[1][num]] == 50:
                environment[(metadata[0][num] + 1)][metadata[1][num]] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[0][num] = metadata[0][num] + 1
                score[num] = score[num] + 1
        except IndexError:
            return metadata, environment, score

    if direction == 1:
        try:
            if environment[metadata[0][num]][(metadata[1][num]+1)] == 0:
                environment[metadata[0][num]][(metadata[1][num]+1)] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[1][num] = metadata[1][num] + 1
            elif environment[metadata[0][num]][(metadata[1][num]+1)] == 50:
                environment[metadata[0][num]][(metadata[1][num]+1)] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[1][num] = metadata[1][num] + 1
                score[num] = score[num] + 1
        except IndexError:
            return metadata, environment, score

    if direction == 2:
        try:
            if environment[(metadata[0][num] - 1)][metadata[1][num]] == 0:
                environment[(metadata[0][num] - 1)][metadata[1][num]] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[0][num] = metadata[0][num] - 1
            elif environment[(metadata[0][num] - 1)][metadata[1][num]] == 50:
                environment[(metadata[0][num] - 1)][metadata[1][num]] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[0][num] = metadata[0][num] - 1
                score[num] = score[num] + 1
        except IndexError:
            return metadata, environment, score

    if direction == 3:
        try:
            if environment[metadata[0][num]][(metadata[1][num]-1)] == 0:
                environment[metadata[0][num]][(metadata[1][num]-1)] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[1][num] = metadata[1][num] - 1
            elif environment[metadata[0][num]][(metadata[1][num]-1)] == 50:
                environment[metadata[0][num]][(metadata[1][num]-1)] = 250
                environment[metadata[0][num]][metadata[1][num]] = 0
                metadata[1][num] = metadata[1][num] - 1
                score[num] = score[num] + 1
        except IndexError:
            return metadata, environment, score

    return metadata, environment, score


def CalculateAction(agents, environment, config, metadata, num, score):

    input_layer = CalculateInputLayer(environment, config, metadata, num)

    hidden_layer = []
    hidden_neuron = 0
    hidden_layer.append(hidden_neuron)

    output_layer = []
    output_neuron = 0
    for i in range(config['output_neurons']):
        output_layer.append(output_neuron)

    network = []
    network.append(input_layer)
    network.append(hidden_layer)
    network.append(output_layer)

    processed_network = CalculateOutputLayer(agents, network, num)

    metadata, environment, score = CalculateMovement(agents, network, metadata, environment, num, score)

    return metadata, environment, score
