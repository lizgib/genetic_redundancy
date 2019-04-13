# just gonna take in my similarity and distance metrics and concetenate them into one big table 

exprs <- read.csv('data/exprs_data/exprs_dat_04-01-2019_norm_NArm.tab', sep = '\t', header = T, row.names = 1)

PCC <- read.csv('outputs/similarity/PCC_mat', sep = '\t', header = T, row.names = 1)
spearmans <- read.csv('outputs/similarity/Spearman_mat', sep = '\t', header = T, row.names = 1)
#MI <- read.csv('outputs/similarity/MI_mat', sep = '\t', header = T, row.names = 1)

#euc <- read.csv('outputs/distance/euc_dist.tab', sep = '\t', header = T, row.names = 1)
PCC_dist <- read.csv('outputs/distance/PCC_dist', sep = '\t', header = T, row.names = 1)

newdf <- data.frame(exprs)
print(row.names(newdf))
#newdf <- cbind(newdf, PCC, spearmans, PCC_dist)

print(length(colnames(newdf))) # if everything is added, it should be something like 
                               # 469 + 5916 + 5916 + 5916 + 5916  = 24133

write.table(newdf, 'outputs/features/feature_table.tab', sep = '\t')

