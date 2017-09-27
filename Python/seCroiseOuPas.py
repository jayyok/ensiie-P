#!/usr/bin/python3

x1 = int(input("x1:\t"))
y1 = int(input("y1:\t"))
x2 = int(input("x2:\t"))
y2 = int(input("y2:\t"))

det = (x1 * y2) - (x2 * y1)

if(det==0):
	print('Les segments ne se croisent pas !')
else:
	print('elles se croisent')