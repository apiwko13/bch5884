import math
# github.com/apiwko13/bch5884

A= input('Enter the x and y coordinates of vertice A separated by a comma:').split(',')
A= [int(i) for i in A]

B= input('Enter the x and y coordinates of vertice B separated by a comma:').split(',')
B= [int(i) for i in B]

C= input('Enter the x and y coordinates of vertice C separated by a comma:').split(',')
C= [int(i) for i in C]

a= math.dist(A,B)
b= math.dist(B,C)
c= math.dist(A,C)

alpha= math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))

beta= math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))

gamma= math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))

print ('The angles alpha, beta, gamma of this triangle are', (alpha, beta, gamma), 'degrees')
