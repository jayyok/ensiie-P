#!/usr/bin/python3

marnage = 10

# Règle des 12
# 1 * 1/12 1
# 1 * 2/12 2
# 2 * 3/12 3-4
# 1 * 2/12 5
# 1 * 1/12 6

# Calcul des marée

def calcSec(h,m,s):
	return (h*3600) + (m*60) + s

# Demande marée basse 
hLow = int(input('Heure de la marée basse :'))
mLow = int(input('Minute de la marée basse :'))
sLow = int(input('Seconde de la marée basse :'))
sizeLow = int(input('Hauteur de la marée basse :'))

# Demande marée Haute 
hHigh = int(input('Heure de la marée haute :'))
mHigh = int(input('Minute de la marée haute :'))
sHigh = int(input('Seconde de la marée haute :'))
sizeHigh = int(input('Hauteur de la marée haute :'))

lastHighSec = calcSec(hHigh, mHigh, sHigh)

def CalculeWaterCycle(hLow,mLow,sLow,hHigh,mHigh,sHigh):
	secondLow = calcSec(hLow,mLow,sLow)
	secondHigh = calcSec(hHigh, mHigh, sHigh)
	return(secondHigh - secondLow)

cycleDuration = 2 *CalculeWaterCycle(hLow,mLow,sLow,hHigh,mHigh,sHigh)

# Demande l'heure voulue

hWanted = int(input('Heure voule :'))
mWanted = int(input('Minute voule :'))
sWanted = int(input('Seconde voule :'))


# Un cycle a une durée de cycleDuration * 2

secondeWanted = calcSec(hWanted,mWanted,sWanted)

# Get the percentage of the currentCycle
percent = ((secondeWanted-lastHighSec)%(cycleDuration)/cycleDuration)


# Chercher le pourcentage dans le cycle courant si > 0.5 alors baisse à partir de marnage sinon augmentation
 
#def GetWaterWithPercent(percent):
#	perce

#def GetPercentMarnage(percent):








