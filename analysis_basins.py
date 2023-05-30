from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv('basins_modified.csv')

df = df.sort_values(by="Distance from South Pole (km)", ascending=True)

print(df)