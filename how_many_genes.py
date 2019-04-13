

f = open('data/genome_data/orf_trans.fasta')

lines = f.readlines()

num_genes = 0
for l in lines:
    print(l)
    if l[0] == '>':
        num_genes +=1
print(num_genes)
