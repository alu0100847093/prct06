

#! encoding: UTF-8
#! /usr/bin/python 
def aproximacion_pi(fin):
 
 if fin>0 :
  suma=0
  for i in range (1,fin+1):
   a=float(i-1)/fin
   b=float (i)/fin
   x_i=float(i-0.5)/fin
   fx_i=float (4)/(1+x_i*x_i)
   suma+=fx_i
  s= suma/fin
 return s
n= int(raw_input('introdusca el numero del factor '))
veces= int(raw_input('introdusca el numero de veces '))

l=[]
for i in range(1,veces+1):
  n*=i
  s=aproximacion_pi(n)
  l=l+[s]
print l
