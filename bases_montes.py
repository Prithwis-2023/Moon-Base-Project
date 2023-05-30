import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("montes_IAU.csv")

names_list = []

for names in df["Clean Feature Name"]:
    names_list.append(names)


for i in range(len(names_list)):
    montes = []
    montes.append(names_list[i])
    montes.append(float(df["Center Latitude"][i]))
    montes.append(float(df["Center Longitude"][i]))
    montes.append(df["Coordinate System"][i])
    montes.append(dist(montes[1], montes[2]))

    with codecs.open('montes.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(montes)
        f.close()    