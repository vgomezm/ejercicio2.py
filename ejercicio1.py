class Cuenta():

    def __init__(self, nombre, saldo):
        self.nombre=nombre
        self.saldo=saldo

    def get_ingreso(self):
        ingresos=self.saldo + 100
        return ingresos

    def get_reintegro(self):
        reintegro=self.saldo-300
        return reintegro

    def get_transferencia(self):
        dinero_tranferido=300
        impuestos=10
        transferencia=self.saldo-300-10
        return transferencia






    
