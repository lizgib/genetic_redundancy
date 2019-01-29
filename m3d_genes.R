
library(tidyverse)

g5520 <- read.delim('data/m3d_data/g5520', sep = ' ')
fitgenes <- read.delim('/mnt/research/ShiuLab/20_Yeast_Redundancy/liz_gene_counts/geneIDS_all', sep = '\t') 

# get only the standard gene name, remove everything else

genename_mat <- str_split_fixed(g5520$gene1, '_', 3)
# this is so dumb... some of the genes are AXXX_YGENE_XX
# and then some of them are like YGENE_XXX

genes_col1 <- genename_mat[,1]
genes_col2 <- genename_mat[,2]

m3d_genes <- unique(c(genes_col1, genes_col2))

length(intersect(m3d_genes, fitgenes$x))

# only going to use genes that are in both my fitness and exprs dataset 

use_genes <- intersect(m3d_genes, fitgenes$x)
length(fitgenes$x[which(!fitgenes$x %in% intersect(m3d_genes, fitgenes$x))])
write.table(use_genes, 'data/m3d_data/m3d_genes', quote = F, sep = '\t')





