import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "restaurante"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def CadastrarPedido(nome_cliente, prato, data_pedido):
    comandoSQL = "SELECT nomecliente, prato, datapedido FROM pedidos"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    pedidos_registrados = [(linha[0], linha[1], linha[2]) for linha in resultado]
    
    if (nome_cliente, prato, data_pedido) in pedidos_registrados:
        print('Pedido já existe para esse cliente, prato e data')
    else:
        comandoSQL = f'INSERT INTO pedidos(nomecliente, prato, datapedido) values("{nome_cliente}", "{prato}", "{data_pedido}")'
        cursor.execute(comandoSQL)
        DBconexao.commit()
        print('Pedido cadastrado com sucesso')

def AlterarPedido(id, novo_prato):
    comandoSQL = "SELECT * FROM pedidos"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    ids = [linha[0] for linha in resultado]
    
    if id in ids:
        comandoSQL = f"UPDATE pedidos SET prato = '{novo_prato}' WHERE idpedidos = {id}"
        cursor.execute(comandoSQL)
        DBconexao.commit()
        print("Pedido alterado com sucesso!")
    else:
        print('ID não encontrado')

def ExcluirPedido(id):
    comandoSQL = "SELECT * FROM pedidos"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    ids = [linha[0] for linha in resultado]
    
    if id in ids:
        comandoSQL = f"DELETE FROM pedidos WHERE idpedidos = {id}"
        cursor.execute(comandoSQL)
        DBconexao.commit()
        print('Pedido excluído com sucesso')
    else:
        print("ID não encontrado")

def PesquisarPedidos(indice, valor):
    if indice == 'data':
        comandoSQL = f"SELECT * FROM pedidos WHERE datapedido = '{valor}'"
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"{i[0]:<5}|{i[1]:<20}|{i[2]:<15}|{i[3]}")
    elif indice == 'cliente':
        comandoSQL = f"SELECT * FROM pedidos WHERE nomecliente = '{valor}'"
        cursor.execute(comandoSQL)
        resultado = cursor.fetchall()
        for i in resultado:
            print(f"{i[0]:<5}|{i[1]:<20}|{i[2]:<15}|{i[3]}")
    else:
        print('Índice não encontrado')

while True:
    print("""
          (1) - Cadastrar Pedido
          (2) - Alterar Pedido
          (3) - Excluir Pedido
          (4) - Pesquisar Pedidos
          (5) - Sair 
          """)

    escolha = int(input("> "))

    if escolha == 1:
        nome_cliente = input("Nome do Cliente: ")
        prato = input("Prato: ")
        data_pedido = input("Data do Pedido (YYYY-MM-DD): ")
        CadastrarPedido(nome_cliente, prato, data_pedido)
    if escolha == 2:
        id = int(input('ID: '))
        novo_prato = input('Novo Prato: ')
        AlterarPedido(id, novo_prato)
    if escolha == 3:
        id = int(input('ID: '))
        ExcluirPedido(id)
    if escolha == 4:
        indice = input('Pesquisar por [cliente/data]: ')
        valor = input('Valor da pesquisa: ')
        PesquisarPedidos(indice, valor)
    if escolha == 5:
        exit()
