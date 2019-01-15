# genetic_redundancy
Scripts written for collaborative genetic redundancy model (worked on in Shiu Lab Fall 2018 - Spring 2019)

The work in this repository is focused particularly on using expression data as features in this model. In addition, 
there are several scripts devoted to the processing of both this expression data and fitness data (obtained from 
Costanzo et al 2016). This data consisted of fitness estimations for pairwise knockouts of ~5700 yeast genes. A single
mutant fitness value was recorded for each gene, as well as a double mutant fitness value for each gene pair. Fitness data
was used to calculate genetic redundancy between two genes (genetic_redundancy.py) based on the following relationship: 



