from Cuenta import Cuenta
#MARCOS BUENO QUINDE
class CuentaCorriente (Cuenta):
    def __init_(self, numero, nombrePropietario, saldo, tieneChequera):
        super().__init__(numero, nombrePropietario, saldo)
        self.tieneChequera = tieneChequera

    @property
    def tieneChequera(self):
        return self.tieneChequera

    @tieneChequera.setter
    def tieneChequera (self, valor):
        self._tieneChequera = valor

    def credito(self, valor):
        if valor > 0:
           self.saldo += valor
           return f"Crédito de ${valor} realizado. Saldo actual: ${self.saldo}
        else:
           return "El valor del crédito debe ser mayor que cero."

    def debito (self, valor):
        if valor > 0 and valor <= self.saldo:
           self.saldo = valor
           return f"Débito de ${valor} realizado. Saldo actual: ${self.saldo}"
        else:
           return "No tiene saldo suficiente para realizar el débito."

    def mostrar_saldo(self):
        return f"Saldo actual de la cuenta corriente: ${self.saldo}"

    def pagar_cheque(self, valor):
        if self.tieneChequera:
            if valor > 0 and valor <= self.saldo:
                self.saldo -=valor
                return f"Pago de cheque por ${valor} realizado. Saldo actual: ${self.saldo}"
            else: