from multiprocessing.spawn import import_main_path
from xml.dom.minidom import Element
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
from calculate_distances import dist
import codecs
'''
data = requests.get('https://en.wikipedia.org/wiki/Far_side_of_the_Moon').text
soup = BeautifulSoup(data, 'lxml')

l = []
l_mod = []
l_craters = []
l_basins = []
l_features = []

for names in soup.find('div', {'class':'div-col'}):
    #print(names)
    names = str(names)
    new = names.split(">")
    for elements in new:
        if "</a" in elements:
            l.append(elements)

for element in l:
    element = element.replace('</a', '')
    if element != '[40]' and element != '[41]':
        l_mod.append(element)

for elements in l_mod:
    if 'crater' in elements:
        new = elements.replace(' (crater)', '')
        l_craters.append(new)
    elif 'lunar crater' in elements:
        new2 = elements.replace(' (lunar crater)', '')
        l_craters.append(new2)    
    elif 'basin' in elements.lower():
        l_basins.append(elements)
    else:
        l_features.append(elements)

for craters in l_craters:
    data2 = requests.get('https://en.wikipedia.org/wiki/{}_(crater)'.format(craters)).text
    soup2 = BeautifulSoup(data2, 'lxml')
    tags = []
    filtered = []
    filtered_copy = []
    final = []
    for text in soup2.findAll('td', {"class":"infobox-data"}):
        tags.append(text)
    try:    
        tags.pop(0)
        tags.pop(-1)
        for element in tags:
            element = str(element)
            newstrg_1 = element.replace('<td class="infobox-data">', '')
            newstrg = newstrg_1.replace('</td', '')
            filtered.append(newstrg)    
        for element in filtered:
            new = element.replace('>', '')
            filtered_copy.append(new)
        filtered_copy.insert(0, craters)
        for coor in soup2.find('span', {'class':'geo-dec'}, {'title':'Maps, aerial photos, and other data for this location'}):
            new = str(coor.text)
            #print(type(new))
            filtered_copy.append(new)    

        for features in filtered_copy:
            if 'Unknown' or 'unknown' in features:
                depth = features.replace('<i', '')
                final_depth = depth.replace('</i', '')
                final.append(final_depth)
            else:
                final.append(features)

        with codecs.open('far_side_craters.csv', 'a', 'utf-8-sig') as f:
            writer_object = writer(f)
            writer_object.writerow(final)
            f.close()

    except IndexError:
        print(craters)            
'''
df = pd.read_csv('far_side_craters.csv')
distances = []
for coor in df["Selenographic Coordinates"]:
    coor = str(coor)
    l = []
    removal = ["°N", "°S", "°E", "°W"]
    m = coor.split(" ")
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
    
    distances.append(dist(l[0], l[1]))
    
for i in range(len(distances)):
    line = "Distance of South Pole from {}: ".format(df.iloc[i]['Crater']) + str(distances[i])+ 'km' 
    with codecs.open('far_side_craters.txt', 'a', 'utf-8-sig') as f:
        f.write(line)
        f.write('\n')
