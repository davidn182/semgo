#%%
from importlib.resources import path
from os.path import exists
import os
path2datadir = os.path.join("Volumes", "Expansion", "kwinstheul",
 "02_data_converted", " 2019")

for i in range(1, 31):
    station_code = "KW" + str(i).zfill(2)
    path2station = os.path.join(path2datadir, station_code)
    for julday in range(173, 312):
        path2julday = os.path.join(path2station, str(julday))
        for hour in range(0, 23):
            hour = str(hour).zfill(2)
            for minute in range(0, 60, 10):
                print(minute)
        for component in ("EHE", "EHN", "EHZ"):
            
            file_name = str(i).zfill(3)
            "_", 
            exists(path_to_file)
# path2station_dir
# file_exists = exists(path_to_file)

# %%
