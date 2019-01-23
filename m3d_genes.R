
setwd('~/Documents/genetic_redundancy/')
library(tidyverse)

g5520 <- read.delim('data/m3d_genes/g5520', sep = ' ')
fitgenes <- read.delim('data/geneIDS_all', sep = '\t') 

# get only the standard gene name, remove everything else
genename5520 <- str_split_fixed(g5520$gene1, '_', 3)

m3d_genes <- unique(genename5520[,2])

length(intersect(m3d_genes, fitgenes$x))
# only going to use genes that are in both my fitness and exprs dataset 
use_genes <- intersect(m3d_genes, fitgenes$x)  

length(fitgenes$x[which(!fitgenes$x %in% intersect(m3d_genes, fitgenes$x))])  

write.table(use_genes, 'data/m3d_genes/m3d_genes', quote = F, sep = '\t')





