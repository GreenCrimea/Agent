traits = {0: 'risk_taking'}

# no reproduction always use mothers traits

def CheckTraitGene(gene):
    if int(gene[0], 16) >= 8:
        return True
    else:
        return False

def ExtractGeneInfoDecimal(gene, index):
    return int(gene[index], 16)

Ext_Dec = ExtractGeneInfoDecimal



def GenerateTraits(genome, config):

    trait_list = {}

    for i in range(len(genome)):
        if CheckTraitGene(genome[i]):
            trait = (Ext_Dec(genome[i], 5) + Ext_Dec(genome[i], 6)) % config['traits']
            trait_name = f'{traits[trait]}'
            if trait_name not in trait_list:
                trait_list[trait_name] = round(((Ext_Dec(genome[i], 1) * 99) + (Ext_Dec(genome[i], 2) * 99)) / 320, 4)
            else:
                if trait_list[trait_name] != round(((Ext_Dec(genome[i], 1) * 99) + (Ext_Dec(genome[i], 2) * 99)) / 320, 4):
                    trait_list[trait_name] = round(((Ext_Dec(genome[i], 1) * 99) + (Ext_Dec(genome[i], 2) * 99)) / 320, 4)

    trait_temp = []
    trait_temp.append(trait_list)
    agent_traits = tuple(trait_temp)
    return agent_traits
