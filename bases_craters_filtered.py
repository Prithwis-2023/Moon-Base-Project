from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("craters.csv")
dist = []
for element in df["Distance from the South Pole (km)"]:
    dist.append(element)

for i in range(len(dist)):
    new_entries = []
    if dist[i] <= 272.847321964273:
        new_entries.append(df["Clean Feature Name"][i])
        new_entries.append(dist[i])
        
        with codecs.open('craters_filtered.csv', 'a', 'utf-8-sig') as f:
            writer_object = writer(f)
            writer_object.writerow(new_entries)
            
