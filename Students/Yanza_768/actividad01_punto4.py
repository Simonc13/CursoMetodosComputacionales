# -*- coding: utf-8 -*-
"""Actividad01_Punto4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZ9rf4-Hor7Q6QEVge87hoxlWK3f4Scu

Actividad 01 Punto 4

Crea una función llamada binomial que reciba dos parámetros llamados n y k. La función debe devolver el coeficiente binomial de n y k, que se define como el número de formas de elegir k elementos distintos de un conjunto de n elementos. Por ejemplo, si n es 5 y k es 3, la función debe devolver 10, ya que hay diez formas de elegir tres elementos distintos de un conjunto de cinco elementos. Llama a la función binomial con diferentes valores para los parámetros n y k, como 6 y 4, o 7 y 2.
"""

# Primero defino una funcion factorial que voy a necesitar para hallar el coeficiente binomial
m = 1
def factorial(n):
  if n == 1:
    return 1
  else:
      return n * factorial(n-1)

# ESTABLEZCO LA FUNCION QUE ME CALCULA EL COEFICIENTE BINOMIAL CON COEF= n!/(k!*(n-k)!)

def binomial(n,k):
  coeficiente = factorial(n) / ((factorial (k)) * factorial (n-k))
  return coeficiente

j1 = binomial(6,4)
print(f"para 6 y 4  el valor es {j1}")

j2 = binomial(7,2)
print(f"para 7 y 2  el valor es {j2}")