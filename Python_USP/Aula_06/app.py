import sqlite3

class Clientes:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, cliente_id, saldo=0):
        self.cliente_id = cliente_id
        self.saldo = saldo
                
    def depositar(self, conn, cursor, valor):
        if valor > 0:
            cursor.execute('UPDATE conta SET saldo = saldo + ? WHERE cliente_id = ?', (valor, self.cliente_id))
            conn.commit()
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print("Valor de depósito inválido.")
                        
    def sacar(self, conn, cursor, valor):
        cursor.execute('SELECT saldo FROM conta WHERE cliente_id = ?', (self.cliente_id,))
        saldo_atual = cursor.fetchone()
        if saldo_atual is not None:
            saldo_atual = saldo_atual[0]
            if saldo_atual >= valor:
                cursor.execute('UPDATE conta SET saldo = saldo - ? WHERE cliente_id = ?', (valor, self.cliente_id))
                conn.commit()
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('Saldo insuficiente. Operação de saque não realizada.')
        else:
            print('Cliente não possui conta.')

def criar_cliente(conn, cursor):
    nome = input('Insira o nome do cliente: ')
    telefone = input('Insira o telefone do cliente: ')
    cursor.execute('INSERT INTO clientes (nome, telefone) VALUES (?, ?)', (nome, telefone))
    conn.commit()
    print("Cliente cadastrado com sucesso.")
    cliente_id = cursor.lastrowid

    # Verificar se o cliente já possui uma conta
    cursor.execute('SELECT id FROM conta WHERE cliente_id = ?', (cliente_id,))
    conta_existente = cursor.fetchone()
    if conta_existente:
        print("O cliente já possui uma conta existente.")
    else:
        cursor.execute('INSERT INTO conta (cliente_id, saldo) VALUES (?, 0)', (cliente_id,))
        conn.commit()
        print("Uma nova conta foi criada para o cliente.")

    return cliente_id

def listar_clientes(cursor):
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    print("\nLista de clientes:")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Telefone: {cliente[2]}")

def opcoes():
    print('\nEscolha uma das opções abaixo:\n')
    print('1. Cadastrar cliente')
    print('2. Listar clientes')
    print('3. Fazer depósito')
    print('4. Fazer saque')
    print('5. Sair')

conn = sqlite3.connect('Banco.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS conta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        saldo REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id))
''')

conn.commit()

opcao = 0
while opcao != 5:
    opcoes()
    opcao = int(input('\nDigite o número da opção desejada: '))

    if opcao == 1:
        cliente_id = criar_cliente(conn, cursor)

    elif opcao == 2:
        listar_clientes(cursor)

    elif opcao == 3:
        listar_clientes(cursor)
        cliente_id = int(input("\nDigite o ID do cliente: "))
        valor_deposito = float(input("\nDigite o valor do depósito: "))
        conta_cliente = Conta(cliente_id)
        conta_cliente.depositar(conn, cursor, valor_deposito)

    elif opcao == 4:
        listar_clientes(cursor)
        cliente_id = int(input("\nDigite o ID do cliente: "))
        valor_saque = float(input("\nDigite o valor do saque: "))
        conta_cliente = Conta(cliente_id)
        conta_cliente.sacar(conn, cursor, valor_saque)

conn.close()


# **Sistema Bancário - Documentação**

# Este é um programa simples de sistema bancário que permite aos usuários realizar operações bancárias básicas, como cadastrar clientes, listar clientes, realizar depósitos e fazer saques. O programa utiliza um banco de dados SQLite para armazenar os dados dos clientes e de suas contas.

# ---

# **Classes:**

# **Clientes:**
# Representa um cliente do banco com atributos como nome e telefone.

# - **Atributos:**
#   - `nome`: Nome do cliente (string)
#   - `telefone`: Número de telefone do cliente (string)

# **Conta:**
# Representa a conta de um cliente com um saldo associado.

# - **Atributos:**
#   - `cliente_id`: ID do cliente associado à conta (inteiro)
#   - `saldo`: Saldo da conta (real)

# - **Métodos:**
#   - `depositar(conn, cursor, valor)`: Realiza um depósito na conta.
#   - `sacar(conn, cursor, valor)`: Realiza um saque na conta.

# ---

# **Funções:**

# **criar_cliente(conn, cursor):**
# Solicita ao usuário que insira o nome e telefone do cliente e insere esses dados na tabela de clientes do banco de dados. Verifica se o cliente já possui uma conta, e se não, cria uma nova conta associada a esse cliente.

# **listar_clientes(cursor):**
# Lista todos os clientes cadastrados no banco de dados.

# **opcoes():**
# Imprime as opções disponíveis para o usuário.

# ---

# **Fluxo Principal:**

# 1. Conectar ao banco de dados SQLite e criar as tabelas de clientes e conta, se elas não existirem.
# 2. Exibir o menu de opções para o usuário.
# 3. Aguardar a entrada do usuário para selecionar uma opção.
# 4. Executar a ação correspondente à opção selecionada pelo usuário.
# 5. Repetir os passos 2-4 até que o usuário selecione a opção para sair do programa.
# 6. Fechar a conexão com o banco de dados ao finalizar o programa.

# ---

# Essa documentação fornece uma visão geral do funcionamento do sistema bancário, incluindo as classes, funções e fluxo principal do programa.