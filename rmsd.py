#https://github.com/apiwko13/bch5884

import sys
import math

#parse pdb file
def readpdb(pdbfilename):
pdbfile=open(pdbfilename,'r')
lines=pdbfile.readlines()
pdbfile.close()

#create dictionary with pdb elements
pdbdict=[]
for line in lines:
    d={}
    d['type']=line[0:6]
    d['anumber']=int(line[6:11])
    d['atype']=line[12:16]
    d['altloc']=line[16:17]
    d['residue']=line[17:20]
    d['chain']=line[21:22]
    d['residuenum']=int(line[22:26])
    d['icode']=str[26:27]
    d['xcoor']=float(line[30:38])
    d['ycoor']=float(line[38:46])
    d['zcoor']=float(line[46:54])
    d['occupancy']=float(line[54:60])
    d['tempfact']=float(line[60:66])
    d['element']=str[76:78].strip()
    d['charge']=str[78:80].strip()
    d['mass']=mass(d['element'])
    pdbdict.append(d)

#mass dictionary for each element type
def getmass(element):
    massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0,"P":30.97,"S":32.07,"MG":24.30}
    mass=massdict.get(element)


#calculate rmsd between two lists
def rmsd(pdbfile1,pdbfile2):
    rmsdsum=0
    n=len(pdbfile1)
for atom in range(len(pdbfile1)):
    x=(pdbfile1[atom]['xcoor']-pdbfile2[atom]['xcoor'])**2
    y=(pdbfile1[atom]['ycoor']-pdbfile2[atom]['ycoor'])**2
    z=(pdbfile1[atom]['zcoor']-pdbfile2[atom]['zcoor'])**2
    rmsdsum += (x+y+z)
    tot_rmsd=sqrt(rmsdsum/n)

    pdb1=readpdb("2FA9noend.pdb") 
    pdb2=readpdb("2FA9noend2mov.pdb")
    rmsd=rmsd(pdb1,pdb2)
print ("The RMSD between the input pdb files is %.2f" % rmsd)
