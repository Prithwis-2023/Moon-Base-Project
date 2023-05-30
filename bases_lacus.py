from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("lacus_IAU.csv")

names_list = []

for names in df["Clean Feature Name"]:
    names_list.append(names)


for i in range(len(names_list)):
    craters = []
    craters.append(names_list[i])
    craters.append(float(df["Center Latitude"][i]))
    craters.append(float(df["Center Longitude"][i]))
    craters.append(df["Coordinate System"][i])
    craters.append(dist(craters[1], craters[2]))

    with codecs.open('lacus.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(craters)
        f.close()    
