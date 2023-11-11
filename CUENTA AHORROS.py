from Cuenta import Cuenta
#MARCOS BUENO QUINDE
class CuentaAhorros (Cuenta):

    def __init_(self, numero, nombre_Propietario, saldo, interes):
        super().__init__ (numero, nombre_Propietario, saldo)
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nueva_interes):
        self._interes = nueva_interes

    def credito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Crédito de ${valor} realizado. Saldo actual: ${self.saldo}"
        else:
            return "El valor del crédito debe ser mayor que cero."

    def debito(self, valor):
        if (valor > 0 and valor <= self.saldo):
            self.saldo += valor
            return f"Débito de ${valor} realizado. Saldo actual: ${self.saldo}"
        else:
            return "No tiene saldo suficiente para realizar el débito."

    def mostrar_saldo(self):
        return f"Saldo actual de la cuenta de ahorros: ${self.saldo}"