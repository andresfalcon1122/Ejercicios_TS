class Transporte:
    @property
    def motor(self):
        return True

    def apagado(self):
        print("motor apagado")

class Terrestre(Transporte):
    pass

class Carro(Terrestre):
    pass

class Moto(Terrestre):
    def motor_chico (self):
        self.apagado()
class Camion(Terrestre):
    pass

carro = Carro()
moto = Moto()
camion = Camion()

print("Carro encendido: \n",carro.motor)
print("\n")
print("Moto encendida: \n", moto.motor_chico())
print("\n")
print("Camion encendido: \n",camion.apagado())
