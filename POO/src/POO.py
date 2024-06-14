'''
NAME
    POO

VERSION
    1.0        

AUTHOR
  Pedro Pineda   

DESCRIPTION
    Programa que muestra un ejemplo de programación orientada a objetos en Python
       
'''

# ===========================================================================
# =                            main
# ===========================================================================


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def haz_ruido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

    def to_dict(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):
    def haz_ruido(self):
        return "Guau"

    def to_dict(self):
        return {
            'tipo': 'perro',
            'nombre': self.nombre,
            'edad': self.edad,
            'onomatopeya': self.haz_ruido()
        }

class Gato(Animal):
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad)
        self.usa_arenero = usa_arenero

    def haz_ruido(self):
        return "Miau"

    def to_dict(self):
        return {
            'tipo': 'gato',
            'nombre': self.nombre,
            'edad': self.edad,
            'usa_arenero': 'sí' if self.usa_arenero else 'no',
            'onomatopeya': self.haz_ruido()
        }

# Crear objetos de las clases Perro y Gato
mi_perro = Perro("Perro sin nombre", 13)
mi_gato = Gato("Gato sin nombre", 1 ,True)

# Imprimir directamente
print(f"Perro: {mi_perro.nombre}, Edad: {mi_perro.edad}.")
print(mi_perro.haz_ruido())
print(f"Gato: {mi_gato.nombre}, Edad: {mi_gato.edad}, Usa arenero: {'Sí' if mi_gato.usa_arenero else 'No'}")
print(mi_gato.haz_ruido())

# Accediendo a través del diccionario
print("Diccionario:")
perro_dict = mi_perro.to_dict()
gato_dict = mi_gato.to_dict()

print(f"Tipo: {perro_dict['tipo']}, Nombre: {perro_dict['nombre']}, Edad: {perro_dict['edad']}")
print(perro_dict['onomatopeya'])
print(f"Tipo: {gato_dict['tipo']}, Nombre: {gato_dict['nombre']}, Edad: {gato_dict['edad']}")
print(gato_dict['onomatopeya'])
