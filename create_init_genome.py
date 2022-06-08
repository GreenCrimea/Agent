'''
CREATE_INIT_GENOME
*****
the generate genome function creates a list of genes for an
agent as defined by the config.
*****
Version: 0.2
Date Last Edited: 8/6/22
*****
Changelog:
    0.2 - added comments and cleaned up
    0.1 - Init commit and basic functionality
'''


import random


def GenerateGenes(bool):                                            # Generate a single gene, with the bool arguement
                                                                    # defining if it is a network or trait gene.
    if bool == 1:                                                   # genes are randomly generated then converted to hex
        min = 0
        max = 7

    else:
        min = 8
        max = 15

    gene_type = f'{random.randrange(min, max):x}'
    gene_info = ''

    for i in range(7):

        gene_info = gene_info + f'{random.randrange(0,15):x}'

    gene = gene_type + gene_info

    return gene


def MutateInit(gene):                                               # Takes a single gene and converts its hex into
                                                                    # binary, then flips a single bit to mutate the
    genes = []                                                      # gene. resulting hex gene bit could have changed
                                                                    # by up to 4 values.
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

    return genes


def GenerateGenome(config):                                         # main function to generate and mutate a genome
                                                                    # for a single agent
    ngene = config['network_genes']
    tgene = config['trait_genes']
    genes = []

    for i in range(ngene):
        gene = GenerateGenes(1)
        genes.append(gene)
        genes.append(gene)

    for i in range(tgene):
        gene = GenerateGenes(0)
        genes.append(gene)
        genes.append(gene)

    genes = MutateInit(genes)

    return genes
