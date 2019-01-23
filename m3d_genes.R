
setwd('~/Documents/genetic_redundancy/')
library(tidyverse)

g5520 <- read.delim('data/m3d_genes/g5520', sep = ' ')
g6954 <- read.delim('data/m3d_genes/g6954', sep = ' ')
g8119 <- read.delim('data/m3d_genes/g8119', sep = ' ')
fitgenes <- read.delim('data/geneIDS_all', sep = '\t') 

genename5520 <- str_split_fixed(g5520$gene1, '_', 3)
genename6954 <- str_split_fixed(g6954$gene2, '_', 3)
genename8119 <- str_split_fixed(g8119$gene3, '_', 3)

# just checked but it looks like all the genes we are working with in the fitness set 
# start with Y
length(fitgenes$x) == length(fitgenes[grep(pattern = 'Y', x = fitgenes$x),])

all_genes <- data.frame(genename5520[grep(pattern = 'Y', x = genename5520[,2]),])
all_genes <- rbind(all_genes, data.frame(genename6954[grep(pattern = 'Y', x = genename6954[,2]),]))
all_genes <- rbind(all_genes, data.frame(genename8119[grep(pattern = 'Y', x = genename8119[,2]),]))

m3d_genes <- unique(all_genes$X2)

length(intersect(m3d_genes, fitgenes$x))
length(fitgenes$x[which(!fitgenes$x %in% intersect(m3d_genes, fitgenes$x))])  
# allright I just tried looking for the genes based on which ones started with Y 
# and I'm getting the exact same numbers so I think im just gonna leave this for 
# now. the number of genes shared between datasets is the same even when I look at it differently
# the only alternative is probably to try splicing them differently. 

# there are 1305 genes missing in this expression dataset
length(m3d_genes[which(!m3d_genes %in% fitgenes$x)])
# 1090 of the m3d_genes are not represented in the fitness data

write.table(genename5520[2], 'data/m3d_genes/g5520', quote = F, sep = '\t')
write.table(genename6954[2], 'data/m3d_genes/g6954', quote = F, sep = '\t')
write.table(genename8119[2], 'data/m3d_genes/g8119', quote = F, sep = '\t')
write.table(m3d_genes, 'data/m3d_genes/m3d_genes', quote = F, sep = '\t')

# allllright have encountered a problem... the m3d genes have kinda messy names. 
# 4400 of them worked just fine but about 1000 of them have funky names that dont 
# work with this current data processing method.. 
# I am thinking of maybe going back and using grep() (looking for each of the gene names 
# from the fitgenes list in the allgenes list) but I think that may be a little time consuming 
# need to go to class but looking at the names of some of the genes being excluded, I think some of 
# those are present in the fitness data and I want them! dont want to unintentionally exclude data




