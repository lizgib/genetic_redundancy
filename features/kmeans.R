#args = commandArgs(TRUE)
#exprs = args[1]
#n = args[2]
#path = args[3]
#path_output = args[4]

exprs = 'data/small_exprs_dat' # NAs need to be removed from this before passing in 
n = '5'
path = 'outputs/clustering/'
path_output = 'test'

setwd('~/Documents/genetic_redundancy/')
dat = read.csv(exprs, sep = '\t',  header = 1, row.names=1)



dat = as.matrix(dat)
dat = as.numeric(dat)

n = as.numeric(n) # number of ks
c1 <- kmeans(dat, n, iter.max = 100, nstart = 50)
list <- as.list(c1$cluster)
# vector <- as.vector(c1$cluster)
# 
write.table(as.matrix(list), path_output, sep="\t", quote = F) # save the cluster IDs to file

