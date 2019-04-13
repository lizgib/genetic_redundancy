'''
grab the gene pairs from the blast output file
'''
import sys, os

gr_gene_pairs = open('data/genome_data/gene_pairs.tab') # these are the gene pairs from the redundancy file
header = gr_gene_pairs.readline()  # going to do a quick interesction to see how many
lines = gr_gene_pairs.readlines()  # gene pairs from there I have in the dup genes (should be near all)

gr_pairs = set()
gr_genes = set()
for l in lines:
    ll = l.strip().split('\t')
    gr_pairs.add(ll[1])
    genes = ll[1].split('_')
    for i in genes:
        gr_genes.add(i)
gr_genes = sorted(gr_genes)

f = open(sys.argv[1])
# f = open('../yeast_blastp_top2_e10.txt')
# outfile = 'e10_dup_genes'
outfile = sys.argv[2]
lines = f.readlines()

out = open(outfile, 'w')
blast_pairs = set()
blast_genes = set()
for l in lines:
    ll = l.strip().split()
    if ll[0] == ll[1]: # if the gene is matching with itsefl i dont care about it dont include
        pass
    else:
        ous = ll[0] + '_' +  ll[1]
        if ous in gr_pairs:
            out.write(ous + '\n')
        blast_genes.add(ll[0]) # adding them to a set so there are no repeats on genes included
        blast_genes.add(ll[1])
        blast_pairs.add(ous)

matchy = gr_pairs.intersection(blast_pairs)
print(len(blast_pairs))
print(len(matchy))
# gene_intersect = gr_genes.intersection(blast_genes)
#print(len(dups), ' # of duplicate genes')

out.close()
