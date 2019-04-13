# this bad boy is just gonna be a quick look at how similar overall 
# the expression levels of all my genes is (expression coherence) 


# expression_coherence = (# of gene pairs w PCC > 0.95)/total # of gene pairs


mat <- read.table('outputs/similarity/PCC_SGD_yeast_expression_dat.02-21-2019.tab', sep = '\t', header = 1, as.is = T)
mat <- as.matrix(mat)
mat <- as.numeric(mat) 
PCC95 <- length(which(mat >= 0.95))
EC <- PCC95/length(mat)
print(EC)





