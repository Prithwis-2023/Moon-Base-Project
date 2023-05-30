from math import radians, cos, sin, asin, sqrt

def dist(lat, lon):
    lon1 = radians(lon)   
    lon2 = radians(0)
    lat1 = radians(lat)    
    lat2 = radians(-90)    #-180 to 180 longitude range
            
    #haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    r = 1737.4 # mean radius of the moon

    return c*r  