class Asiento:
    def __init_(self, color, precio, registro):
        self.color= color
        self.precio= precio
        self.registro = registro
    def cambiarColor(self,color):
        if (color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
            return self.color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
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
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio= precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        contarAsientos=0
        for asiento in self.asientos:
            if(asiento!=None):
                contarAsientos+=1
        return contarAsientos
    def verificarIntegridad(self):
        if(self.registro==self.motor.registro):
            for i in self.asientos:
               if(i!=None):
                    if(i.registro!=self.registro):
                        return "Las piezas no son originales" 
            return "Auto original"
        else:
            return "Las piezas no son originales"
