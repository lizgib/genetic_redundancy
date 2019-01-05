#commands_kmeans
#quick_kmeans_for various k
#kmeans.R file should be in the same directory as wd

import sys, os

expression_data = sys.argv[1]  # this is gonna be my redundancy data: fitness_only_26.csv 
output_file = sys.argv[2] # just gonna call this: redun_26_ 
path = sys.argv[3] # going to put these in the outputs folder in a subdir 'outputs/clustering_outputs'
type = sys.argv[4] #to label your output file

oup=open("commands_kmeans_%s" % type, "w" )

b = [3, 6, 9, 27, 90, 150, 300, 450, 750, 1200] # I have changed these to be multiples of 3 since we expect 3 outcomes 

#for j in range(1, 11):
for i in b:
    k = int(i)
    output_file2 = output_file+"k"+str(k)+ "_%s" % type
    oup.write("R --vanilla --slave --args\t%s\t%i\t%s\t%s\t<\tkmeans.R\n" %(expression_data, k, path, output_file2))
oup.close()

'''
import sys, os
files_path = sys.argv[1]
#.rstrip("/")
code = sys.argv[2]
go = sys.argv[3]
a = sys.argv[4]
oup=open("commands_enrichment_%s" % a ,"w" )
for file in os.listdir(files_path):
    if file.startswith("genelist"):
        file_name = file.strip().split("_")
        kmeans = file_name[1][0]
        type = file_name[2]
        run = int(file_name[3][3])
        file1 = files_path+file
        oup.write("python\t%s\t%s\t%s\t%i\t%s\t%s\n" % (code, file1, go, run, kmeans, type)) 
#python ../goenrichment_cluster.py genelist_k1000_stressint_run2 ~/1_Expression_Database/GO/updated_go_gene_012013 2 k strint
oup.close()
'''

