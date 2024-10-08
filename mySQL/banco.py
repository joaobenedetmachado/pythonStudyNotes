import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "vendas"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

# CRUD - CREATE

def InsertDB(nome, valor):
  comandoSQL = f'INSERT INTO produtos (nomeproduto, valorproduto) values ("{nome}", {valor})'
  cursor.execute(comandoSQL)
  DBconexao.commit()
  print(f"Criado {nome} com valor de {valor} com sucesso")

# CRUD - READ

def ReadDB():
  comandoSQL = f"SELECT * FROM produtos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall() 
  print()
  for i in resultado:
    print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<10.2f}")
  print()
    
# CRUD - UPDATE

def UpdateDB(tabela, novoValor, condicao):
  comandoSQL = f'UPDATE produtos SET {tabela} = "{novoValor}" where idproduto = {condicao}'
  cursor.execute(comandoSQL)
  DBconexao.commit()
  print(f"Alterado com sucesso")
  
# CRUD - DELETE

def DeleteDB(id):
  comandoSQL = f"DELETE FROM produtos WHERE idproduto = {id}"
  cursor.execute(comandoSQL)
  DBconexao.commit()
  print(f"ID: {id} Excluido com sucesso")


while True:
  print("1 - Inserir produto")
  print("2 - Alterar produto")
  print("3 - Excluir produto")
  print("4 - Ler produto")

  escolha = input("> ")
  
  if escolha == "1":
    nomeproduto = input("Digite o nome do novo produto: ")
    valorproduto = float(input("Digite o valor do novo produto: "))
    InsertDB(nomeproduto, valorproduto)
    
  if escolha == "2":
    tabela = input("Qual tabela deseja alterar [nomeproduto / valorproduto]?:  ")
    condicao = int(input("Digite o id que deseja alterar: "))

    comandoSQL = f"SELECT * FROM produtos"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()  

    ids_existentes = [linha[0] for linha in resultado] 

    if condicao in ids_existentes:
        novoValor = input(f"Novo valor para o {tabela}: ").title()
        UpdateDB(tabela, novoValor, condicao)
    else:
        print(f"ID {condicao} não encontrado")

    
  if escolha == "3":
    idproduto = int(input("Digite o id do produto que deseja excluir: "))
    DeleteDB(idproduto)
  
  if escolha == "4":
    ReadDB()
