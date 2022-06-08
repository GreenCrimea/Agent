'''
CREATE_INIT_TRAITS
*****
the create traits function will decode the infomation in
trait genes, and determine the trait value
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


traits = {0: 'risk_taking'}


def CheckTraitGene(gene):                                           # check that a gene is encoding a trait

    if int(gene[0], 16) >= 8:

        return True

    else:

        return False


def ExtractGeneInfoDecimal(gene, index):                            # Converts the individual gene bits into decimal

    return int(gene[index], 16)

Ext_Dec = ExtractGeneInfoDecimal


def GenerateTraits(genome, config):                                 # generate traits by decoding their value from genes

    trait_list = {}                                                 # TRAIT = (GENE * 99) = (GENE * 99) / 320

    for i in range(len(genome)):                                    # right now if theres multiple trait genes, only the
                                                                    # last indexed gene is used
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
