#-*-coding: utf-8 -*-
def bisiesto (fecha):
	if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
		print ("El ano", fecha, "es un ano bisiesto.")
	else:
		print ("El ano", fecha, "no es un ano bisiesto.")
 
print("Comprobador de años bisiestos")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))
bisiesto (fecha)
