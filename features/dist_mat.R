
# this script is just gonna calculate basic euclidean distance between 
# gene expression levels using the dist function in R 

exprs <- read.table('data/SGD_yeast_expression_dat.02-21-2019.NAremove.tab', sep = '\t', header = 1, row.names = 1, as.is = T)
exprs <- as.matrix(exprs) 
exprs <- as.numeric(exprs)
f <- dist(exprs)
write.csv(f, 'outputs/distance/euc_dist.tab', sep = '\t')


# 3/20 I tried something else and it ran, but not sure it was computed correctly \
# the above kept giving me a memory error saying that dist mat was too big to allocate 
# so i tried this instead and it appears to have run?? 

dat <- read.csv('data/SGD_yeast_expression_dat.02-21-2019.NAremove.tab',sep = '\t', header = 1)
mat <- dist(dat)
o <- as.matrix(mat)
write.table(o, 'outputs/temp_euc_dist_shell.tab', sep = '\t', quote = F)

# still need to check the calculations on this, but this may work???


