class Asiento:
    def init(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro = registro
    def cambiarColor(self,color):
        color=str(input())
        if (color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
            return self.color

class Motor:
    def init(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo= tipo
        self.registro= registro
    def cambiarRegistro(self,registro):
        self.registro= registro
        return self.registro
    def asignarTipo(self,tipo):
        if(tipo=="electrico" or tipo=="gasolina"):
            self.tipo = tipo
            return self.tipo
        
class Auto:
    cantidadCreados=0
    def _init_(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio= precio
        self.asientos = []
        self.marca = marca
        self.motor = Motor
        self.registro = registro
    def cantidadAsientos(self):
        contarAsientos=0
        for i in range(len(asientos)):
            if(asientos[i]!=None):
                contarAsientos+=1
        return contarAsientos
    def verificarIntegridad(self):
        if(registro==motor.registro):
            for i in range(len(asientos)):
               if(asientos[i]!=None):
                    if(asientos[i].registro!=registro):
                        return print("Las piezas no son originales") 
            return print("Auto original")
        else:
            return print("Las piezas no son originales")
