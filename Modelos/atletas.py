from Modelos.planes import Plan
class Atleta:
    nombre:str
    apellido:int
    nivel:int
    fecha_nac:str
    plan: Plan

    def __init__(self,nombre,apellido,nivel,fecha_nac,plan=None):
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel
        self.fecha_nac = fecha_nac
        self.plan = plan

    def __str__(self):

        return f"Nombre: {self.nombre} \n Apellido: {self.apellido} \n Nivel: {self.nivel} \n Fecha de Nacimiento: {self.fecha_nac} \n Plan: {self.plan}"