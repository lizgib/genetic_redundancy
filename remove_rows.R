
library(tidyverse)
# going to take out rows that have genes I am not planning on using 

# read in the files 
#filename <- readline(prompt = 'Filename: ')
#filename <- 'data/m3d_data/avg_Yeast_Genome_S98_v2_exps247probes5520.tab'
filename <- 'data/m3d_data/avg_Yeast_Genome_S98_v2_exps247probes5520.tab'
f <- read.delim(filename, sep = '\t', row.names = 1) 
genes <- read.delim('data/m3d_data/m3d_genes', sep = '\t')

# make this column match the format of the m3d genes (just the Y--- genename)
genename_mat <- str_split_fixed(row.names(f), '_', 3)

genes_col1 <- genename_mat[,1]
genes_col2 <- genename_mat[,2]

f$genes_col1 <- genes_col1
f$genes_col2 <- genes_col2

# grab only rows which are in the m3d_genes 
for (i in 1:nrow(f)){
  if (f[i,'genes_col1'] %in% genes$x){
    f[i, 'gene'] <- f[i, 'genes_col1']
  }
  if (f[i,'genes_col2'] %in% genes$x){
    f[i, 'gene'] <- f[i, 'genes_col2']
  }
}

# make a new dataframe for the genes with these indices
newdf <- f[!is.na(f$gene),] # if no gene was placed in the column it will just be NA
row.names(newdf) <- newdf$gene
newdf$genes_col1 <- NULL
newdf$genes_col2 <- NULL
newdf$gene <- NULL
newmat <- as.matrix(newdf)

png('exp_heatmap.png')
heatmap(newmat)
dev.off()

outname <- paste('data/yeast_expression_dat.', Sys.Date(), '.tab', sep = '')
write.table(newdf, outname, quote = F, sep = '\t')


