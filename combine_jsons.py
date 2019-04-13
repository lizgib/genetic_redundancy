'''
i have a shit ton of json files now i gotta put them all in one big df
'''

import sys,os

os.chdir('data/json_files/test')
for jsn in os.listdir(os.getcwd()):
    
