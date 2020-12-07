#

import scipy
from scipy.optimize import curve_fit
import numpy as np
from numpy import corrcoef
from matplotlib import pylab as plt



#user required inputs
#conc=input('What is the concentration of enzyme in the assay? (mM)')
#totalvolume=input('What is the assay volume? (mL)')
#ext=input('What is the molar extinction coefficient of your measured product?')
#subs=input('What substrate are you measuring?')
#title=input('Provide a title for your experiment')

#inputs that I used from my own data to run the code
conc=0.0000425
ext=6220
totalvolume=1
subs=('Shikimate')
title=('MtSK Shikimate Assay')


#read csv file and output fitted data
f=open('Assay.csv', 'r', encoding='utf-8-sig')
lines=f.readlines()
f.close

#create lists for x, y values and append them into arrays
v=[]
S=[]

for i in lines:
    words=i.split(',')
    v.append(float(words[1]))
    S.append(float(words[0]))

x=np.array(S)
y=np.array(v)
ndata=len(x)

#define the Michaelis Menten Equation to use as a model
def model (x, Vmax, Km):
    return Vmax*x/(x+Km)

#Use curve fit to calculate Km and Vmax and fit data to equation
popt,_=curve_fit(model,x,y)
Vmax,Km=popt

actual_Vmax=Vmax; actual_Km=Km

initialGuess=[1,1]
parameters,covar=curve_fit(model, x, y, absolute_sigma=True, p0=initialGuess)

#plot of user input data
plt.errorbar(x,y,fmt='bs', capsize=5)
plt.scatter(x,y)

#plot of MM curve
t=np.linspace(0,max(x))
plt.plot(t,model(t,*parameters))

#output of Vmax and Km
print('Vmax= %.4f AU/min' %Vmax)
print('Km= %.4f mM' %Km)

#kcat calculation and output
Kcat=(Vmax/60/ext/conc)*(totalvolume*1000)
print('Kcat= %.4f 1/s' %Kcat)


#catalytic efficiency calculation and output
Keff= Kcat/Km
print('catalytic efficiency=%.4f' %Keff)

#R squared calculation and output using polyfit to calculate ssreg and sstotal
def polyfit(x,y,degree):
    results={}

    coeffs=np.polyfit(x,y,2)
    polynomial=coeffs.tolist()
    p=np.poly1d(coeffs)
    yhat=p(x)
    ybar=np.sum(y)/len(y)
    ssreg=np.sum((yhat-ybar)**2)
    sstot=np.sum((y-ybar)**2)
    results['R squared']=ssreg/sstot

    return results

print(polyfit(x,y,2))

#Plot data fitted to curve with user input substrate on x axis label
plt.title(title)
plt.xlabel('%s (mM)' %subs)
plt.ylabel('Rate (AU/min)')
plt.show()

#HTML output
Html_file= open('MMfit.html','w')
data='''<html>
<head></head>
<body><img src="plt.show()">
Vmax
Km
Kcat
Keff
polyfit(x,y,2)
</body>
</html>'''
Html_file.write(data)
Html_file.close


