#! encoding: UTF-8
#! /usr/bin/python 
def aproximacion_pi(inicio,fin):
 n=0
 f=1
 while n>0 and f==1:
  f+=1
  suma=0
  for i in range (1,n+1):
   a=float(i-1)/n
   b=float (i)/n
   x_i=float(i-0.5)/n
   fx_i=float (4)/(1+x_i*x_i)
   suma+=fx_i
   s= suma/n
 return s