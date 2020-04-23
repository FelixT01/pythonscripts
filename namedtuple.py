#!/bin/python3.7
import collections
from functools import reduce
from operator import add
from itertools import chain
class MedicalRecord:
	def merge(*args): #recive una lista de cosas
		Data = collections.namedtuple('paciente',reduce(add,(x._fields for x in args)))
		#reduce(operacion, lista) realiza una operacion a las cosas de una lista. 
		#se recorre la lista de parametros y se sacan los fields de los namedtuple
		data = Data(*chain(*args))
		#chain  une cosas. si entra p y q, una lista de p0, p1...pn, q0,q1..
		return data


Persona = collections.namedtuple('yo',['nombre','edad','genero'])
Enfermedad = collections.namedtuple('enfermedades',['dengue','malaria','sida'])

pipol = Persona('felix',29,'macho')
enfeimo = Enfermedad(dengue='si', malaria='si',sida='no')

lista1=[1,2,3]
lista2=[4,5,6]

x = MedicalRecord
def juntai(*args):
	print (*chain(*args))

juntai(lista1,lista2)
print (x.merge(pipol,enfeimo))
