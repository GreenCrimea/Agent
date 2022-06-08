import random

def GenerateGenes(bool):
    if bool == 1:
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


def MutateInit(gene):
    genes = []
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



def GenerateGenome(config, agents, Score):

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
