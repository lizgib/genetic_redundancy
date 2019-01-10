
setwd('~/Documents/genetic_redundancy/')
library(tidyverse)

g5520 <- read.delim('data/m3d_genes/g5520', sep = ' ')
g6954 <- read.delim('data/m3d_genes/g6954', sep = ' ')
g8119 <- read.delim('data/m3d_genes/g8119', sep = ' ')

genename5520 <- str_split_fixed(g5520$gene1, '_', 3)[,2]
genename6954 <- str_split_fixed(g6954$gene2, '_', 3)[,2]
genename8119 <- str_split_fixed(g8119$gene3, '_', 3)[,2]

allgenes <- unique(c(genename5520, genename6954, genename8119))

fitgenes <- read.delim('data/geneIDS_all', sep = '\t')

length(intersect(allgenes, fitgenes$x))
length(fitgenes$x[which(!fitgenes$x %in% intersect(allgenes, fitgenes$x))])  
# there are 1305 genes missing in this expression dataset
length(allgenes[which(!allgenes %in% fitgenes$x)])
# 1090 of the m3d_genes are not represented in the fitness data

write.table(genename5520, 'data/m3d_genes/g5520', quote = F, sep = '\t')
write.table(genename6954, 'data/m3d_genes/g6954', quote = F, sep = '\t')
write.table(genename8119, 'data/m3d_genes/g8119', quote = F, sep = '\t')
write.table(allgenes, 'm3d_genes', quote = F, sep = '\t')

# allllright have encountered a problem... the m3d genes have kinda messy names. 
# 4400 of them worked just fine but about 1000 of them have funky names that dont 
# work with this current data processing method.. 
# I am thinking of maybe going back and using grep() (looking for each of the gene names 
# from the fitgenes list in the allgenes list) but I think that may be a little time consuming 
# need to go to class but looking at the names of some of the genes being excluded, I think some of 
# those are present in the fitness data and I want them! dont want to unintentionally exclude data




