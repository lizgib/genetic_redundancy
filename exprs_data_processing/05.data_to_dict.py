'''
this script we are going to pull each expression condition out of the main file
and put it in its own dictionary like so...

condition = {GENE1: EXP_LEVEL, GENE2: EXP_LEVEL, GENE3: EXP_LEVEL,...}

these dictionaries will then be written out to json file

'''


import pandas as pd
import json
import sys, os

# if its a dist mat youre putting in json, specify

#f = 'outputs/similarity/PCC_mat'
f = sys.argv[1]
#outname = 'PCC'
outname = sys.argv[2]

df = pd.read_csv(f, sep = '\t', index_col = 0, header = 0)
data_dict = df.to_dict()
for d in data_dict:
    outfile = open('%s/%s.json' %(outname,d), 'w')
    json.dump(data_dict[d], outfile, indent=4, sort_keys=True)

# os.chdir('data/json_files/similarity/%s' %outname)
# outie = open('all%s.json' %outname, 'w')
# all_files = {}
# for jsn in os.listdir(os.getcwd()):
#     gene = jsn.split('.')[0]
#     json_file = open(jsn)
#     json_str = json_file.read()
#     exprs_data = json.loads(json_str)
#     print(exprs_data)
# #    pairwise_dict = {}
#     for k in exprs_data.keys():
#         pair = gene + '_' + k
# #        pairwise_dict[pair] = exprs_data[k]
#         all_files[pair] = exprs_data[k]
# #    outfile = open(jsn, 'w')
# #    json.dump(pairwise_dict, outfile, indent = 4, sort_keys = True)
# json.dump(all_files, outie, indent = 4, sort_keys = True)
