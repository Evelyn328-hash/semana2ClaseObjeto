class CuentaBancaria:
    def __init__(self, titular, tipo_cuenta, saldo=0):
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
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
    def mostrar_información(self):
        print(f"El propietario de la cuenta es: {self.titular}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
# Ejemplo de uso
cuenta = CuentaBancaria("Evelyn Montes", "Ahorros", 2000)
cuenta.mostrar_información()
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(1500)
cuenta.mostrar_saldo()
# Ejemplo de uso
cuenta2 = CuentaBancaria("Patricia Quinatoa", "Corriente", 1000)
cuenta2.mostrar_información()
cuenta2.mostrar_saldo()
cuenta2.depositar(-300)
cuenta2.retirar(200)
cuenta2.mostrar_saldo()