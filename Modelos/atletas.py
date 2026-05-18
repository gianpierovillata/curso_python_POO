class Atleta:
    nombre:str
    apellido:int
    nivel:int
    fecha_nac:str

    def __init__(self,nombre,apellido,nivel,fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel
        self.fecha_nac = fecha_nac

    def __str__(self):

        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Nivel: {self.nivel} \n Fecha de Nacimiento: {self.fecha_nac}"