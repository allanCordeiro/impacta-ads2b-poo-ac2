# Programação Orientada a Objetos
# AC02 ADS-EaD - Implementação de classes
# Allan Cordeiro
# Email Impacta: allan.cordeiro@aluno.faculdadeimpacta.com.br

class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo_inicial
        self.__ativa = False
        self.__operacoes = []
        self._gravar_operacao('saldo inicial', self.__saldo)

    # property blocks
    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, valor):
        if isinstance(valor, bool):
            self.__ativa = valor

    def depositar(self, valor):
        if self._validar_condicoes(valor):
            self.__saldo += valor
            self._gravar_operacao('deposito', valor)
            return True
        return False

    def sacar(self, valor):
        if self._validar_condicoes(valor):
            if self.saldo >= valor:
                self.__saldo -= valor
                self._gravar_operacao('saque', valor)
                return True
        return False

    def transferir(self, conta_destino, valor):
        if conta_destino.ativa:
            if self._validar_condicoes(valor) and self.saldo >= valor:
                conta_destino.__saldo += valor
                self.__saldo -= valor
                self._gravar_operacao('transferencia', valor)
                # conta_destino._gravar_operacao('transferencia', valor)
                return True
        return False

    def tirar_extrato(self):
        return self.__operacoes

    def _gravar_operacao(self, operacao, valor):
        self.__operacoes.append((operacao, valor))

    def _validar_condicoes(self, valor):
        if self.ativa and valor > 0:
            return True
        return False