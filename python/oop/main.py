class Main:
    pass

from cliente import Cliente
from conta import Conta


c1= Cliente("Lucas", "1234-5678")
conta=Conta(c1.nome,0,6565)

conta.deposito(100)
conta.saque(50)
conta.extrato()

print(conta.titular,"Número da conta:",conta.numero,"Saldo:",conta.saldo)