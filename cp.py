#github.com/apiwko13/bch5884
#PDB file read/write code


import matplotlib
import math
import statistics

#open file for reading

f=open('2FA9noend.pdb', 'r')
lines=f.readlines()

#PARSING FILE INTO DICTIONARY

records=[]

massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}

for line in lines:
    atomdict={}

#elements of pdb file parsed by position into dictionary

    e1=str(line[0:5])
    e2=str(line[6:11])
    e3=str(line[12:16])
    e4=str(line[17:20])
    e5=str(line[21])

    e6=int(line[22:26])
    
    x=float(line[30:38])
    y=float(line[39:46])
    z=float(line[47:54])

    e7=float(line[55:60])
    e8=float(line[61:66])

    element=line[76:78].strip()

    mass=massdict[element]

    records.append([e1,e2,e3,e4,e5,e6,x,y,z,e7,e8,element,mass]) #pdb format

#MASS CENTER CALCULATIONS

#creating new variables to calculate mass averaged coordinates, trying to use the sum() operation was what was giving me trouble earlier
    
totalmass=0
xmass=0
ymass=0
zmass=0

for record in records:
    totalmass+=record[12]
    xmass+=record[12]*record[6]
    ymass+=record[12]*record[7]
    zmass+=record[12]*record[8]

#mass center=coordinated-weighted mass/total mass of all atoms
    
xmc=xmass/totalmass
ymc=ymass/totalmass
zmc=zmass/totalmass

#GEOMETRIC CENTER CALCULATIONS

#same process as mass calculations, except averaging each coordinate point

xcoors=0
ycoors=0
zcoors=0
totalpts=len(records)

for record in records:
    xcoors+=record[6]
    ycoors+=record[7]
    zcoors+=record[8]
    
xavg=xcoors/totalpts
yavg=ycoors/totalpts
zavg=zcoors/totalpts

#With all calculations done, choice of output is given to user:

choice=input("Do you want to center by mass or geometry 'M' or 'G': " )
if choice=="M":
    f=open('MC.pdb', 'w')
    for e in records:
            s="{0:6}{1:6}{2:5}{3:4}{4:1}{5:4}{6:12.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}{11:>12}\n" #assigning writeout positions/length of numbers
            f.write(s.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6]-xmc,e[7]-ymc,e[8]-zmc,e[9],e[10],e[11]))
    f.close()
    print('done! the mass-centered file is in your current directory')
    pass
elif choice=="G":
    f=open('GC.pdb', 'w')
    for e in records:
        s="{0:6}{1:6}{2:5}{3:4}{4:1}{5:4}{6:12.3f}{7:8.3f}{8:8.3f}{9:6.2f}{10:6.2f}{11:>12}\n"#3 decimals for coordinates, 2 decimals for masses
        f.write(s.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6]-xavg,e[7]-yavg,e[8]-zavg,e[9],e[10],e[11]))
    f.close()
    print('done! the geometrically-centered file is in your current directory')
    pass



