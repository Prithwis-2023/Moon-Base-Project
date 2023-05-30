import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("valles_IAU.csv")

names_list = []

for names in df["Clean Feature Name"]:
    names_list.append(names)


for i in range(len(names_list)):
    valles = []
    valles.append(names_list[i])
    valles.append(float(df["Center Latitude"][i]))
    valles.append(float(df["Center Longitude"][i]))
    valles.append(df["Coordinate System"][i])
    valles.append(dist(valles[1], valles[2]))

    with codecs.open('valles.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(valles)
        f.close()    