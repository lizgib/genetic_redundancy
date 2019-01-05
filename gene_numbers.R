
SGA_all <- read.csv('/mnt/research/ShiuLab/20_Yeast_Redundancy/00_Raw_Data/Raw_SGA_Data.csv')
SGA_26 <- read.csv('/mnt/research/ShiuLab/20_Yeast_Redundancy/00_Raw_Data/Raw_SGA_Data_26.csv')
SGA_30 <- read.csv('/mnt/research/ShiuLab/20_Yeast_Redundancy/00_Raw_Data/Raw_SGA_Data_30.csv')

SGA_all$Query_geneIDS <- gsub('_.*', '', SGA_all$Query.Strain.ID)
print(SGA_all$Query_geneIDS)
SGA_26$Query_geneIDS <- gsub('_.*', '', SGA_26$Query.Strain.ID)
print(SGA_26$Query_geneIDS)
SGA_30$Query_geneIDS <- gsub('_.*', '', SGA_30$Query.Strain.ID)
print(SGA_30$Query_geneIDS)

SGA_all$Array_geneIDS <- gsub('_.*', '', SGA_all$Array.Strain.ID)
SGA_26$Array_geneIDS <- gsub('_.*', '', SGA_26$Array.Strain.ID)
SGA_30$Array_geneIDS <- gsub('_.*', '', SGA_30$Array.Strain.ID)
  
# total number of gene IDS (query + array)
geneIDs_all <- union(SGA_all$Query_geneIDS, SGA_all$Array_geneIDS)
geneIDs_26 <- union(SGA_26$Query_geneIDS, SGA_26$Array_geneIDS)
geneIDs_30 <- union(SGA_30$Query_geneIDS, SGA_30$Array_geneIDS)

# total number of QUERY gene IDs 
query_geneIDs_all <- unique(SGA_all$Query_geneIDS)
query_geneIDs_26 <- unique(SGA_26$Query_geneIDS)
query_geneIDs_30 <- unique(SGA_30$Query_geneIDS)

# total numbr of ARRAY gene IDs

array_geneIDs_all <- unique(SGA_all$Array_geneIDS)
array_geneIDs_26 <- unique(SGA_26$Array_geneIDS)
array_geneIDs_30 <- unique(SGA_30$Array_geneIDS)


print(paste('The total number of genes is: ', length(geneIDs_all)))
print(paste('The total number of genes in the 26 dataset is: ', length(geneIDs_26)))
print(paste('The total number of genes in the 30 dataset is: ', length(geneIDs_30)))


print(paste('The total number of query genes is: ', length(query_geneIDs_all)))
print(paste('The total number of query genes in the 26 dataset is: ', length(query_geneIDs_26)))
print(paste('The total number of query genes in the 30 dataset is: ', length(query_geneIDs_30)))


print(paste('The total number of array genes is: ', length(array_geneIDs_all)))
print(paste('The total number of array genes in the 26 dataset is: ', length(array_geneIDs_26)))
print(paste('The total number of array genes in the 30 dataset is: ', length(array_geneIDs_30)))



