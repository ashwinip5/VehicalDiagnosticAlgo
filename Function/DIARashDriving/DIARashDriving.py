# Rash Driving detection
import pandas as pd

def detect_rash_driving(lat, long, pos_d, pos_e, Threshold):
    x=[]
    y=[]
    z=[]

    for i in range(0, len(lat)):
        if (float(pos_d[i]) > Threshold) and (float(pos_e[i]) > Threshold / 2):
            x.append(lat[i])
            y.append(long[i])
            z.append(i)
    d = {'Latitude': x, 'Longitude': y, 'Index': z}
    df = pd.DataFrame(data=d)
    return df;
