def Mutate(gene):
    genes = []
    rand_chance = 2 #random.randrange(0,4)
    if rand_chance == 2:
        for i in range(len(gene)):
            if i % 2 == 0:
                int_gene = int(gene[i], 16)
                binary_gene = f'{int_gene:0>32b}'
                rand_num = random.randrange(0,30)
                binary_bitflip = ('0' * rand_num) + '1' + ('0' * (31 - rand_num))
                mutated = int(binary_gene, 2) ^ int(binary_bitflip, 2)
                genes.append(f'{mutated:0>8x}')
            else:
                genes.append(gene[i])
    else:
        genes = gene
    return genes



def Evolve(agents, score, config):

    total_score = 0
    new_agents = []

    for i in range(len(agents)):

        total_score = total_score + score[i]

    avg_score = total_score / len(agents)

    for i in range(len(agents)):
        if score[i] > ((avg_score + 0.1) * 2):
            for a in range((10+len(agents)-1)//10):
                if len(new_agents) < len(agents):
                    new_agents.append(agents[i])
                else:
                    break

    if len(new_agents) < len(agents):
        for i in range(len(agents)):
            if score[i] > ((avg_score + 0.1)* 1.5):
                for a in range((25+len(agents)-1)//25):
                    if len(new_agents) < len(agents):
                        new_agents.append(agents[i])
                    else:
                        break

    if len(new_agents) < len(agents):
        for i in range(len(agents)):
            if score[i] >= (avg_score):
                for a in range((50+len(agents)-1)//50):
                    if len(new_agents) < len(agents):
                        new_agents.append(agents[i])
                    else:
                        break

    if len(new_agents) < len(agents):
        for i in range(len(agents)):
            rm = random.randrange(0, len(agents))
            if len(new_agents) < len(agents):
                new_agents.append(agents[rm])
            else:
                break

    for a in range(len(new_agents)):
        genes = []

        for i in range(len(new_agents[a][1])):
            genes.append(new_agents[a][1][i])

        genes = Mutate(genes)
        new_agents[a][1] = genes

        brain = GenerateBrain(genes, config)
        new_agents[a][2] = brain

        traits = GenerateTraits(genes, config)
        new_agents[a][3] = traits


    return new_agents
