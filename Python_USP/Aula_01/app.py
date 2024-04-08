def criar_arquivo():
    conteudo_do_arquivo = ("""
1000 capital inicial\n
-500 compra de matéria - prima\n
-200 mao de obra\n
400 venda do primeiro lote\n
300 venda do segundo lote\n
-300 aluguel da fabrica\n
    """)
    with open("financeiro.log", "w") as arquivo:
        arquivo.write(conteudo_do_arquivo)

  
def calcular_saldo():
    saldo = 0
    with open("financeiro.log") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                valor = int(linha.split()[0])
                saldo += valor
    exibicao_do_financeiro = print(f"\nO saldo financeiro da empresa e de: {saldo}\n")
    return exibicao_do_financeiro

def nova_linha():

    contador = 0
    while contador == 0:
        print('Gostaria de adicionar dados ao arquivo (sim) ou (nao) ?')
        adicionar_arquivo = input().lower()

        if adicionar_arquivo != "sim" and adicionar_arquivo != "nao":
            print('\nComando incorreto, por favor digite um comando válido\n')
            contador == 0

        elif adicionar_arquivo == "nao":
            print('\nOk. Programa encerrado!')
            contador = 1

        else:
            contador = 1
            novo_valor = input('\nInsira o valor: ')
            nova_descricao = input('\nInsira a descrição: ')
            with open("financeiro.log", "a") as arquivo:
                novos_dados = (f'{novo_valor} {nova_descricao}\n')
                arquivo.write(novos_dados)
            calcular_saldo()
               
               
criar_arquivo()
calcular_saldo()
nova_linha()