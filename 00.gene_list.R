library(seqinr)

setwd( "~/Documents/FS18/PLB498/data/")

fasta_file <- read.fasta('~/Documents/FS18/PLB498/data/orf_genomic.fasta')
gene_list <- getName(fasta_file)
gene_list <- as.factor(gene_list)
write.csv('../outputs/yeast_gene_list.csv')
