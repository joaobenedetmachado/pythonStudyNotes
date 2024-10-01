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
  

nomeproduto = input("Digite o nome do novo produto: ")
valorproduto = float(input("Digite o valor do novo produto: "))

InsertDB(nomeproduto, valorproduto)

# CRUD - UPDATE

def UpdateDB(tabela, novoValor, condicao):
  comandoSQL = f'UPDATE produtos SET nomeproduto = "{novoValor}" where idproduto = {condicao}'
  cursor.execute(comandoSQL)
  DBconexao.commit()
  
tabela = input("Qual tabela deseja alterar [nomeproduto / valorproduto]?:  ")
condicao = int(input("Digite o id que deseja alterar: "))
novoValor = input(f"Novo valor para o {condicao}: ").title()

UpdateDB(tabela, novoValor, condicao)

