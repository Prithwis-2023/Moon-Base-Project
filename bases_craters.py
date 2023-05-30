from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from calculate_distances import dist
from csv import writer
import codecs

df = pd.read_csv("craters_IAU.csv")

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

    with codecs.open('craters.csv', 'a', 'utf-8-sig') as f:
        writer_object = writer(f)
        writer_object.writerow(craters)
        f.close()    



'''
ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letters in ls:        
    df = pd.read_csv('craters_{}.csv'.format(letters))
    least_dist = []
    for coor in df["Coordinates"]:
        coor = str(coor)
        new = coor.split(" / ")
        main_coor =new[1]
        main = main_coor.replace('\ufeff', '')
        l = []
        m = main.split(" ")
        removal = ["°N", "°S", "°E", "°W"]
        for i in range(len(m)):
                if removal[0] in m[i]:
                    new = m[i].replace(removal[0], "")
                    new = float(new)
                    l.append(new)             
                
                elif removal[1] in m[i]:
                    new = m[i].replace(removal[1], "")
                    new = -float(new)
                    l.append(new)

                elif removal[2] in m[i]:
                    new = m[i].replace(removal[2], "")
                    new = float(new)
                    l.append(new)

                elif removal[3] in m[i]:
                    new = m[i].replace(removal[3], "")
                    new = -float(new)
                    l.append(new)
                
        least_dist.append(dist(l[0], l[1]))
    
    for i in range(len(least_dist)):
        final = []
        final.append(df.iloc[i]['Crater'])
        final.append(least_dist[i])
        #line = "Distance of South Pole from {}: ".format(df.iloc[i]['Crater']) + str(least_dist[i])+ 'km' 
        with codecs.open('craters.csv', 'a', 'utf-8-sig') as f:
            writer_object = writer(f)
            writer_object.writerow(final)
            f.close()                              
'''
