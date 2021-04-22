#TU_VILLANO_FAVORITO

import datetime 


def get_villain_name(name, birthdate):
  nombre = get_nombre(birthdate)
  segundo_nombre = get_segundo_nombre(name)
  apellido = get_apellido(birthdate)
  return nombre_completo(nombre,segundo_nombre,apellido)

def nombre_completo(nombre,segundo_nombre,apellido):
	return nombre + " " + segundo_nombre + " " + apellido 

def get_nombre(birthdate):
   mes_nacimiento = birthdate.month
   return get_nombre_segun_mes(mes_nacimiento)

def get_segundo_nombre(name):
	nombre_invertido = invertir_nombre(name)
	nombre_minusculas = nombre_invertido.lower() #Convierte todo el nombre en minusculas
	segundo_nombre = nombre_minusculas.title() #Convirtiendo el nombre al formato titulo, la primera letra de cada nombre será mayúscula.
	return segundo_nombre

def get_apellido(birthdate):
    dia_nacimiento = birthdate.day
    ultimo_digito_dia = get_ultimo_digito(dia_nacimiento)
    return get_apellido_segun_digito(ultimo_digito_dia)

def get_ultimo_digito(numero):
	cadena_ultimo_digito = str(numero) #convierte la fecha de nacimiento en una cadena
	ultimo_digito = int(cadena_ultimo_digito[-1]) #convierte el ultimo digito de la cadena en un entero
	return ultimo_digito

def invertir_nombre(name):
    nombre_invertido = ""
    for letra in name:
        nombre_invertido = letra + nombre_invertido
    return nombre_invertido

#Para devolver un villain name según el mes indicado, se diseña un "Switch": 
def enero():
    return "The Evil"
 
def febrero():
    return "The Vile"
 
def marzo():
    return "The Cruel"
 
def abril():
    return "The Trashy"
 
def mayo():
    return "The Despicable"
 
def junio():
    return "The Embarrassing"
 
def julio():
    return "The Disreputable"
 
def agosto():
    return "The Atrocious"
 
def septiembre():
    return "The Twirling"
 
def octubre():
    return "The Orange"
 
def noviembre():
    return "The Terrifying"
 
def diciembre():
    return "The Awkward"
 
def get_nombre_segun_mes(argument):
    switch = {
    1: enero(),
    2: febrero(),
    3: marzo(),
    4: abril(),
    5: mayo(),
    6: junio(),
    7: julio(),
    8: agosto(),
    9: septiembre(),
    10: octubre(),
    11: noviembre(),
    12: diciembre()
 }
    return switch.get(argument)

#Para devolver un villain surname segun el ultimo digito de nacimiento también genero otro "Switch":
def cero():
	return "Mustache"

def uno():
	return "Pickle"

def dos():
	return "Hood Ornament"

def tres():
	return "Raisin"

def cuatro():
	return "Recycling Bin"

def cinco():
	return "Potato"

def seis():
	return "Tomato"

def siete():
	return "House Cat"

def ocho():
	return "Teaspoon"

def nueve():
	return "Laundry Basket"

def get_apellido_segun_digito(digito):
  switcher = {
  0: cero(),
  1: uno(),
  2: dos(),
	3: tres(),
	4: cuatro(),
  5: cinco(),
  6: seis(),
	7: siete(),
  8: ocho(),
  9: nueve()
 }
  return switcher.get(digito)