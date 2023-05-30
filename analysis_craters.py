from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs
import matplotlib.pyplot as plt

df = pd.read_csv("craters.csv")

df = df.sort_values(by="Distance from the South Pole (km)", ascending=True)

print(df)