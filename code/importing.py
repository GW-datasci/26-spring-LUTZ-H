import os
import glob
import csv
import pandas as pd

print("current wd:", os.getcwd())
datadir = "../data/"
arabdir = "../data/arabbarometer/alldata/"
afrodir = "../data/afrobarometer/alldata/"
americasdir = "../data/americasbarometer/"

# for saving all of the outputted dfs from imports
dfs = {}
# just using alldata subdirs, but also my computer crashed upon trying to load americasbarometer (oops!)
exclude_dirs = {"extras", "americasbarometer"}
# os.walk returns 3-tuple of root, subdirs, and files in them
for root, dirs, files in os.walk(datadir): 
    # thank you stackexchange <3; removes exclude_dirs
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        path = os.path.join(root, file)
        name = os.path.splitext(file)[0]  # [1] is extension but theres other ways of dealing with that
        print(name)
        if (file.endswith(".csv")):
            dfs[name] = pd.read_csv(path)
            print("csv done")
        elif (file.endswith(".dta")):
            dfs[name] = pd.read_stata(path)
            print("dat done")
        elif (file.endswith(".sav")):
            dfs[name] = pd.read_spss(path)
            print("sav done")

# print("done!")

