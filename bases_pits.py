from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv('lunar_pits.csv')
names = []
for row in df["Name"]:
    names.append(row)
for i in range(len(names)):
    data = []
    lat = float(df['Lat.'][i])
    long = float(df['Long.'][i])
    data.append(names[i])
    data.append(lat)
    data.append(long)
    data.append(dist(lat, long))
    
    with codecs.open('pits.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(data)
        f.close()  
    
