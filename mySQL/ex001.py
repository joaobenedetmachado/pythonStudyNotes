import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "carros"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def InsertDB(nome, marca, modelo, ano, cor):
  comandoSQL = f"SELECT * FROM carros"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  nomes_existentes = [linha[1] for linha in resultado] 
  if nome in nomes_existentes:
    print(f"Carro {nome} ja existe")
  else:
    comandoSQL = f'INSERT INTO carros (marca, modelo, ano, cor) values ("{marca}", "{modelo}", {ano}, "{cor}")'
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Criado {nome} com sucesso")
    
def DeleteDB(id):
  comandoSQL = f"DELETE FROM carros WHERE idcarros = {id}"
  cursor.execute(comandoSQL)
  DBconexao.commit()
  print(f"ID: {id} Excluido com sucesso")

def SearchDB(indice, valor):
  comandoSQL = f"SELECT * FROM carros WHERE {indice} = '{valor}'"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall() 
  for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<10} | {i[3]:<10} | {i[4]:<10}")

  
while True:
  print("1 - Inserir")
  print("2 - Deletar")
  print("3 - Buscar")
  print("4 - Sair")
  escolha = int(input("> "))
  
  if escolha == 1:
    nome = input("Nome: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    InsertDB(nome, marca, modelo, ano, cor)
  
  if escolha == 2:
    id = int(input("ID: "))
    DeleteDB(id)
  
  if escolha == 3:
    indice = input("Indice: ")
    valor = input("Valor: ")
    SearchDB(indice, valor)

  if escolha == 4:
    exit()