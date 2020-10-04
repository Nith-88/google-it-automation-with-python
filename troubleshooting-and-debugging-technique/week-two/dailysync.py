# Fixing a slow system with python using multiprocessing and subprocess module

#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool
os.chdir('../data/')
list=[]
for path,dir,file in os.walk('prod/'):
        list.append(dir)
list=list[0]
def backup(list):
        src = "../data/prod/"+str(list)
        dest = "../data/prod_backup/"
        subprocess.call(["rsync", "-arq", src, dest])
if __name__=="__main__":
        p=Pool(len(list))
        p.map(backup,list)
