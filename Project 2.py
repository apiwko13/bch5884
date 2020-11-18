#!/usr/bin/env python3

import numpy as np
from scipy.signal import find_peaks, peak_widths, peak_prominences, argrelextrema


#open and read the file
f=open("superose6_50.asc", 'r')
lines=f.readlines()
f.close()

#create lists for the time and abs values 
time=[]
absorb=[]

for i in lines[3:]:
    words=i.split()
    try:
        time.append(float(words[0]))
        absorb.append(float(words[1]))
    except:
        print('the file was parsed')
        continue

#create aray of values
    
t=np.array(time)
a=np.array(absorb)

#baseline appears to be at ~30, set peak threshold to 50 
threshold=50

#create lists for peak coordinates
peaks=[]
centroid=[]
peaks_coor=[]
points=[]

#compares a, b, c values to find maxima and appends found peak values to new list
for i in range((len(absorb))-1):
    d=absorb[i-1]
    e=absorb[i]
    f=absorb[i+1]
    if e>=d and e>=f and e>threshold:
        peaks.append(absorb[i])
        centroid.append(time[i])
        peaks_coor.append((time[i],absorb[i]))
        points.append(i)


#print coordinates of peaks        
print("The peaks are at the following (time(min), absorbance(mAU)) values:")
print(peaks_coor)

#find slope at all points
slope=[]
for i in range((len(a))-1):
    dx=t[i+1]-t[i]
    dy=a[i+1]-a[i]
    slope.append(dy/dx)




#find dips in between peaks
dipx=[]
dipy=[]

for i in range(len(points)-1):
	list_time=t[points[i]:points[i+1]]
	list_abs=a[points[i]:points[i+1]]
	
	avalues=np.array(list_abs)
	
	inverse=1/avalues
	
	dips,_=find_peaks(inverse)
	
	dipx.append(float(list_time[dips]))
	dipy.append(float(list_abs[dips]))


#defining start and end points
	
start_x=[]
start_y=[]

end_x=[]
end_y=[]

n=points[0]-5

#if slope is greater, start point will be appended, vice versa for end point

while(slope[n]>5):
    n=n-1
start_x.append(float(t[n-4]))
start_y.append(float(a[n-4]))


k=points[len(points)-1]
while(slope[k+5]<-5):
    k=k+1
end_x.append(float(t[k+4]))
end_y.append(float(a[k+4]))

#printing boundary results

print("The boundaries of peak 1 are", start_x[0],"to",dipx[0],"mins")
print("The boundaries of peak 2 are",dipx[0],"to",dipx[1],"mins")
print("The boundaries of peak 3 are",dipx[1],"to",dipx[2],"mins")
print("The boundaries of peak 4 are",dipx[2],"to",end_x[0],"mins")







