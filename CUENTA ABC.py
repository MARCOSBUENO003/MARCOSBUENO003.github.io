from abc import ABC
#MARCOS BUENO QUINDE
class Cuenta (ABC):
    def __init_(self, numero, nombrePropietario, saldo, credito, debito):
        self._numero= numero
        self._nombrePropietario = nombrePropietario
        self._saldo = saldo
        self._credito = credito
        self._debito = debito


    @property
    def numero(self):
        return self._numero


    @numero.setter
    def numero(self, nuevo_numero):
        self._numero= nuevo_numero

    @property
    def nombrePropietario(self):
        return self._nombrePropietario


    @nombrePropietario.setter
    def nombrePropietario (self, nuevo_nombre):
        self._nombrePropietario = nuevo_nombre

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, nuevo_saldo):