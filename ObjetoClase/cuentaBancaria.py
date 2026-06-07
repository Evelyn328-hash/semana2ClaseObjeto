class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else: 
                print("Fondos insuficientes para realizar el retiro.")
        else: 
            print("La cantidad a retirar debe ser mayor que cero.")

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")

 