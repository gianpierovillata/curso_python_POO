class Book:
    def __init__(self, autor:str,nombre:str, isbn:str, editorial:str, publicacion:int, disponible:bool):
        self.autor = autor
        self.nombre = nombre
        self.isbn = isbn
        self.editorial = editorial
        self.publicacion = publicacion
        self.disponible = disponible

    def __str__(self):
        return f"Autor: {self.autor}\nNombre: {self.nombre}\nISBN: {self.isbn}\nEditorial: {self.editorial}\nPublicacion: {self.publicacion}\nDisponible: {self.disponible}"



#definir un libro
libro1 = Book("Gabriel Garcia Marquez", "Cien Años de Soledad", "978-3-16-148410-0", "Editorial Sudamericana", 1967, True)

print(libro1)

#definir una lista de libros
libros =[]

libro2 = Book("J.K. Rowling", "Harry Potter y la Piedra Filosofal", "978-3-16-148410-1", "Editorial Salamandra", 1997, True)

libros.append(libro1)
libros.append(libro2)


for libro in libros:
    print(f"Nombre: {libro.nombre}, Autor: {libro.autor}, Disponible: {libro.disponible}")
    print("-------------")


# informacion de datos del deportista

from pandas import DataFrame
class DatosSalud:
    def __init__(self, actividad, tiempo, frecuencia_media, frecuencia_maxima, calorias,distancia):
        self.actividad = actividad
        self.tiempo = tiempo
        self.frecuencia_media = frecuencia_media
        self.frecuencia_maxima = frecuencia_maxima
        self.calorias = calorias
        self.distancia = distancia

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso} kg\nAltura: {self.altura} m"


datos1 = DatosSalud("Correr", "30 minutos", 120, 150, 300, 5)
datos2 = DatosSalud("Nadar", "45 minutos", 110, 140, 400, 1)

datos_salud = [datos1, datos2]

df = DataFrame([vars(datos1), vars(datos2)])
print(df)

