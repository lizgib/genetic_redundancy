# genetic redundancy 

# gr = (s1 + s2 - dmf) / abs(dmf)

f <- read.csv('data/fitness_data/clean/clean_DMF_matrix26_3.14.2019.tab', sep = '\t', header = 1)

# im a dumbass i need to do this on the selection coefficient not the raw fitness!!! 
#  selection_coefficient = (SMFx - 1)/1

f$S1 <- (f$SMF1 - 1)/1
f$S2 <- (f$SMF2 - 1)/1
f$SD <- (f$DMF - 1)/1

f$num <- f$S1 + f$S2 - f$SD
f$genetic_redundancy <- f$num/ abs(f$SD)

outname <- paste('genetic_redundancy_26_', Sys.Date(), '.tab', sep = '')
write.table(f, outname, sep = '\t', quote = F, row.names = F)

graph_name = paste('genetic_redundancy_26', Sys.Date(), '.pdf', sep = '')
pdf(graph_name)
hist(f$genetic_redundancy)
dev.off()
