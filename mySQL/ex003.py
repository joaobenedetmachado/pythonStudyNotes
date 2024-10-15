import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "loja"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def CadastrarProduto(nome, categoria, quantidade):
  comandoSQL = f"SELECT * FROM produtos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  nomes_existentes = [linha[1] for linha in resultado]
  categorias_existentes = [linha[2] for linha in resultado] 
  if nome not in nomes_existentes and categoria not in categorias_existentes:
    comandoSQL = f"INSERT into produtos(nome, categoria, quantidade) values('{nome}', '{categoria}', '{quantidade}')"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"produto {nome} cadastrado com sucesso")
  else:
    print("Produto com tal categoria ja existe")
    
def AlterarQuantidade(id, quantidade):
  comandoSQL = f"SELECT * FROM produtos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids_existentes = [linha[0] for linha in resultado]
  if id in ids_existentes:
    comandoSQL = f"UPDATE produtos SET quantidade = '{quantidade}' where idprodutos = {id}"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Alterado com sucesso")
  else:
    print("ID não encontrado")

def DeletarProduto(id):
  comandoSQL = f"SELECT * FROM produtos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids_existentes = [linha[0] for linha in resultado]
  if id in ids_existentes:
    comandoSQL = f"DELETE FROM produtos WHERE idprodutos = {id}"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Deletado com sucesso")
  else:
    print("ID não encontrado")
    
def ListarProdutos():
  comandoSQL = f"SELECT * FROM produtos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<10}|{i[3]:>5}")
    
while True:
  print("""
        (1) - Inserir
        (2) - Alterar
        (3) - Excluir
        (4) - Buscar
        (5) - Sair 
        """)
  
  escolha = int(input("> "))
  
  if escolha == 1:
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))
    CadastrarProduto(nome, categoria, quantidade)
    
  if escolha == 2:
    
    id = int(input("ID: "))
    quantidade = int(input("Quantidade: "))
    AlterarQuantidade(id, quantidade)
    
  if escolha == 3:
    id = int(input("ID: "))
    DeletarProduto(id)
    
  if escolha == 4:
    ListarProdutos()
    
  if escolha == 5:
    exit()

    