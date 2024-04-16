# Enunciado do exercício:
# Você foi contratado(a) em um banco e precisa representar, no seu programa, a conta de diferentes clientes.
# Por abstração, assuma que:
# Cada cliente possui nome e telefone.
# Cada conta possui um cliente e um saldo*.
# As operações que podem ser feitas na conta são saque (diminui o saldo) e depósito (aumenta o saldo).

# * Não se esqueça que o saque só é possível se o valor dele estiver disponível na conta. Se for possível retirar sem ter o saldo, então o banco iria à falência!




# Enunciado do exercício:
# Vamos aperfeiçoar o exercício da aula passada, considerando agora um novo tipo de conta: a conta poupança. Ela é projetada para acumular economias a longo prazo, então é comum existir restrições sobre o número de saques que podem ser feitos em um determinado período.
# A conta poupança é uma extensão da conta padrão. Continua com os atributos sendo o cliente e o saldo, mas agora também temos a necessidade de limitar o número de saques que podem ser feitos. Considere que o número limite de saques é um novo atributo.

# Dica: inclua um atributo contador que é somado sempre que um saque é realizado

class Clientes:
        def __init__(self, nome, telefone):
                self.nome = nome
                self.telefone = telefone


class Conta:
        def __init__(self, cliente, saldo = 0):
                self.cliente = cliente
                self.saldo -= saldo

        def deposito(self, valor):
                self.saldo += valor 
                print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")


        def saque(self, valor):
                if self.saldo >= valor:
                        self.saldo -= valor
                        print(f'Saque no valor de {valor} realizado com sucesso. Novo saldo: {self.saldo}')
                else:
                        print('Saldo insuficiente. Operacao de saque nao realizada.')


class ContaPoupanca(Conta):
            def __init__(self, cliente, saldo = 0, limite_saques= 3):
                    super().__init__(cliente, saldo)
                    self.limite_saques = limite_saques
                    self.saques_realizados = 0

            
            def saque(self, valor):
                    if self.saques_realizados < self.limite_saques:
                            super().saque(valor)
                            self.saques_realizados += 1
                            print(f"Saques realizados no mês: {self.saques_realizados}/{self.limite_saques}")
                    else:
                            print("Limite de saques excedido para este mês.")


class ListaClientes:
        def __init__(self):
                self.clientes = []

        def adicionar_clientes(self, cliente):
                self.clientes.append(cliente)

        def listar_clientes(self):
                for cliente in self.clientes:
                        print(f'Nome: {cliente.nome} Telefone: {cliente.telefone}')


def cadastrar_clientes():
        nome = input('insira o nome do cliente: ')
        telefone = input('Insira o telefone do cleinte :')
        return Clientes(nome, telefone)


def realizar_transacao(conta):
        pass
        


def transacao():
        pass


def opcoes():
        print('1. Adicionar cliente')
        print('2. Listar clientes')
        print('3. Realizar transacao')
        print('4. Excluir cliente')
        print('5. Sair')

        escolha_inicial = input()
        if escolha_inicial == '1':
                cadastrar_clientes()

print()
lista_clientes = ListaClientes()
lista_clientes.listar_clientes()
