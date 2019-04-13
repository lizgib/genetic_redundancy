# processing blast output 
args = commandArgs(TRUE)
dupfile = args[1]
eval = args[2]

gr <- read.csv('data/gene_redun/binned_genetic_redundancy_2019-03-15.tab', sep = '\t')
dup = read.csv(dupfile, sep = '\t', header = F)

dup$pair <- paste(dup$V1, '_', dup$V2, sep = '')

newdf <- gr[!is.na(match(gr$Pair, dup$pair)),]
fname =paste('data/dup_genes_eval_', eval, '2019-04-04.tab', sep = '')
write.table(newdf, fname, sep = '\t', header = 1)

plotname = paste('dup_genes_evalue_', eval, 'gr.pdf', sep = '')
pdf(plotname)
hist(newdf$bin, breaks = nrow(newdf))
dev.off()

plotname = paste('dup_genes_evalue_', eval, 'fit.pdf', sep = '')
pdf(plotname)
hist(newdf$fit, breaks = nrow(newdf))
dev.off()
print(nrow(newdf))

