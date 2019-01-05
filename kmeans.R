args = commandArgs(TRUE)
exprs = args[1]
n = args[2]
path = args[3]
path_output = args[4]


setwd(path)
 
exprs = as.matrix(exprs)
exprs = read.csv(exprs, header=T,row.names=1)
 
n = as.numeric(n)
# 
# 
# c1 <- kmeans(exprs, n, iter.max = 100, nstart = 50)
# list <- as.list(c1$cluster)
# vector <- as.vector(c1$cluster)
# 
# write.table(as.matrix(list), path_output, sep="\t") 

exprs <- as.matrix(exprs[2:nrow(exprs), c('Query_SMF', 'Array_SMF', 'DMF')])
# ^^B this is the format for the file we are clustering... I dont have the rownames which concerns me, but 
# the order of everything should be preserved, and when Dante has everything sorted, I will feel even better about things


c1 = kmeans(exprs, n, iter.max = 100, nstart = 50)

list <- as.list(c1$cluster)
vector <- as.vector(c1$cluster)

write.table(as.matrix(list), path_output, sep="\t")


