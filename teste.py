import  atividade_conta

conta = atividade_conta.Conta('Allan', '123', '123', 50)
conta_2 = atividade_conta.Conta('Jose', '1', '567', 0)
conta.ativa = True
conta_2.ativa = True
print(f"Status da conta: {conta.ativa}")
print(f"depositar {conta.depositar(100)}")
print(conta.transferir(conta_2, 50))
print(conta.tirar_extrato())
print(conta.saldo)
print(conta_2.saldo)
print(conta_2.tirar_extrato())
print(conta.tirar_extrato())
