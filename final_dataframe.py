'''
Ive had enough of this. Im just gonna put everything ina big dataframe
that i can run through the pipeline. fukc json it seems cool but these scripts are
taking forever
'''

import sys, os
import pandas as pd
import json

os.chdir('outputs/features/min_max_avg')
all_files = {}
for jsn in os.listdir(os.getcwd()):
    fname = jsn.split('.')[0]
    json_file = open(jsn)
    json_str = json_file.read()
    exprs_data = json.loads(json_str)
    for pair in exprs_data.keys():
        if pair not in all_files.keys():
            all_files[pair] = []
        for v in exprs_data[pair]:
            all_files[pair].append(v)
print(all_files[pair])

outfile = open('../json_USEME_final_df.tab', 'w')
out = open('../USEME_final_dataframe.tab', 'w')
json.dump(all_files, outfile, indent=4, sort_keys=True)

plast = 'arbitrarykey'
for p in all_files.keys():
    out.write(p)
    for v in all_files[p]:
        print(v)
        out.write(v)
        out.write('\t')
        if p != plast:
            out.write('\n')
            plast = p
out.close()

# os.chdir('outputs/features/similarity/PCC')
# for jsn in os.listdir(os.getcwd()):
#     fname = jsn.split('.')[0]
#     json_file = open(jsn)
#     json_str = json_file.read()
#     exprs_data = json.loads(json_str)
#     for pair in exprs_data.keys():
#         if pair not in all_files.keys():
#             all_files[pair] = []
#         for v in exprs_data[pair]:
#             all_files[pair].append(v)
#
# os.chdir('outputs/features/similarity/Spearman')
# for jsn in os.listdir(os.getcwd()):
#     fname = jsn.split('.')[0]
#     json_file = open(jsn)
#     json_str = json_file.read()
#     exprs_data = json.loads(json_str)
#     for pair in exprs_data.keys():
#         if pair not in all_files.keys():
#             all_files[pair] = []
#         for v in exprs_data[pair]:
#             all_files[pair].append(v)
#
# os.chdir('outputs/features/similarity/euc')
# for jsn in os.listdir(os.getcwd()):
#     fname = jsn.split('.')[0]
#     json_file = open(jsn)
#     json_str = json_file.read()
#     exprs_data = json.loads(json_str)
#     for pair in exprs_data.keys():
#         if pair not in all_files.keys():
#             all_files[pair] = []
#         for v in exprs_data[pair]:
#             all_files[pair].append(v)
#
# os.chdir('outputs/features/similarity/PCC_dist')
# for jsn in os.listdir(os.getcwd()):
#     fname = jsn.split('.')[0]
#     json_file = open(jsn)
#     json_str = json_file.read()
#     exprs_data = json.loads(json_str)
#     for pair in exprs_data.keys():
#         if pair not in all_files.keys():
#             all_files[pair] = []
#         for v in exprs_data[pair]:
#             all_files[pair].append(v)

#pd.DataFrame.from_dict(data=all_files, orient='index').to_csv(('../min_max_avg_feature_table.tab'), header=False, sep = '\t')
# write the dictionary out to a table
