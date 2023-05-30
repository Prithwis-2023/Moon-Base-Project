from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("rupes_IAU.csv")

names_list = []

for names in df["Clean Feature Name"]:
    names_list.append(names)


for i in range(len(names_list)):
    basins = []
    basins.append(names_list[i])
    basins.append(float(df["Center Latitude"][i]))
    basins.append(float(df["Center Longitude"][i]))
    basins.append(df["Coordinate System"][i])
    basins.append(dist(basins[1], basins[2]))

    with codecs.open('rupes.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(basins)
        f.close()    
