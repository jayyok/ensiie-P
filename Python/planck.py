#!/usr/bin/python3
import math


h=6.6256e-34
C=2.998e+8
K=1.38054e-2
pi=math.pi

tempKelvin = float(input('Veuillez entrer la température en kelvin (20°=273.15K) : '))
waveLength = float(input('longueur d\'onde : '))

E = (2.00*pi*h*C**2)*waveLength**-5
Z = (math.exp(((h*C)/(K*tempKelvin))/waveLength)-1.0)
if(Z!=0):
	E = E / Z
	print('Answer : ' + str((math.exp(((h*C)/(K*tempKelvin))/waveLength)-1.0)) + ' (W/m²)')	
else:
	print('Your waveLength suck !')