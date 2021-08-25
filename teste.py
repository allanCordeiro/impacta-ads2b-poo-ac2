import  atividade_conta

conta = atividade_conta.Conta('Allan', '123', '123', 50)
# conta.ativa = True
print(conta.depositar(100))
print(conta.sacar(150))
print(conta.operacoes)