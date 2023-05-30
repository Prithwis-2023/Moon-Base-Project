from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv('maria.csv')

distances = []
names = []

for elements in df["Distance from the South Pole (km)"]:
    distances.append(elements)

for elements in df["Clean Feature Name"]:
    names.append(elements)

fig = plt.figure(figsize = (100, 100))

plt.scatter(names, distances)
plt.xlabel("Maria")
plt.ylabel("Distance from South pole (km)")
plt.show()