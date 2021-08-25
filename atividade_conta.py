# Programação Orientada a Objetos
# AC02 ADS-EaD - Implementação de classes
# Allan Cordeiro
# Email Impacta: allan.cordeiro@aluno.faculdadeimpacta.com.br


class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self._titular = titular
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo_inicial
        self._ativa = False
        self._operacoes = []
        self._gravar_operacao('saldo inicial', self._saldo)

    def _gravar_operacao(self, operacao, valor):
        self._operacoes.append((operacao, valor))

    # property blocks
    @property
    def titular(self):
        return self._titular

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativa(self):
        return self._ativa

    @ativa.setter
    def ativa(self, valor):
        if isinstance(valor, bool):
            self._ativa = valor
