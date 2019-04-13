'''
grab column maximum, minimum, and averaage
from each gene pair in each treatment
3/28/2019
'''
import pandas as pd
import sys, os
import json


os.chdir('data/json_files/raw_exprs')
all_files = {}
#outfile = open('../../../outputs/features/mma_all.json', 'w')
dup = pd.read_csv('../../../blast_stuff/e10_dup_genes', sep = '\t', header = None, index_col = False, squeeze = True)
dup_list = dup.tolist()
out = open('../../../outputs/features/dup_mma_all_write.tab', 'w')

all_files['gene'] = ['diff', 'min', 'max', 'avg']
for jsn in os.listdir(os.getcwd()):
    fname = jsn.split('.')[0]
    json_file = open(jsn)
    json_str = json_file.read()
    exprs_data = json.loads(json_str)
    # pairwise_dict = {} # this is just some bullshit from when i was writing out each json file to its own file still
    # outfile = open('../../../outputs/features/min_max_avg/mma_%s.json' %fname, 'w')
    for i in exprs_data.keys():
        for j in exprs_data.keys():
            pair = i + '_' + j
            if pair in dup_list:
                if pair not in all_files.keys():
                    all_files[pair] = []
                vals = [exprs_data[i], exprs_data[j]]
                vals = sorted(vals)
                diff = vals[1] - vals[0]
                mini = min(vals)
                maxi = max(vals)
                avg = sum(vals)/2
                # pairwise_dict[pair].extend([diff, mini, maxi, avg])
                all_files[pair].append(diff)
                out.write(pair)
                out.write('\t')
                out.write(str(diff))
                out.write('\t')
                all_files[pair].append(mini)
                out.write(str(mini))
                out.write('\t')
                all_files[pair].append(maxi)
                out.write(str(maxi))
                out.write('\t')
                all_files[pair].append(avg)
                out.write(str(avg))
                out.write('\n')
    json_file.close()

    # json.dump(pairwise_dict, outfile, indent=4, sort_keys=True)
#json.dump(all_files, outfile, indent=4, sort_keys=True)
pd.DataFrame.from_dict(data=all_files, orient='index').to_csv(('../../../outputs/features/dup_mma_all.tab'), header=False, sep = '\t')
out.close()
# make a dictionary of each gene pair (for i in keys: for j in keys: i_j)
    # need to check if the reciprocal gene pair has already been added
    # need to only add the duplicate genes

# iterate through the keys in this pairwise dictionary
# for each gene pair, grab the original
    # difference between the two
    # which one was the bigger value
    # which was smaller value
    # what was the average between teh two
