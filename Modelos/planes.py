from datetime import date, timedelta

class Plan:
    id: int
    nombre: str
    descripcion: str
    duracion: int
    fecha_inicio: date
    fecha_fin: date
    objetivos: str

    def __init__(self, id, nombre, descripcion, duracion, fecha_inicio, fecha_fin, objetivos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.fecha_inicio = date.today()
        self.fecha_fin = date.today() + timedelta(days=duracion)
        self.objetivos = objetivos


    def __str__(self):
        return f"ID: {self.id} \n Nombre: {self.nombre} \n Descripcion: {self.descripcion} \n Duracion: {self.duracion} dias \n Fecha de Inicio: {self.fecha_inicio} \n Fecha de Fin: {self.fecha_fin} \n Objetivos: {self.objetivos}"