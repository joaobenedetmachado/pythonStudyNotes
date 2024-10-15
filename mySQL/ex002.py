import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "empresa"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def InsertDB(nome, cargo):
  comandoSQL = f"SELECT * FROM funcionarios"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  nomes_existentes = [linha[1] for linha in resultado]
  cargos_existentes = [linha[2] for linha in resultado] 
  if nome in nomes_existentes and cargo in cargos_existentes:
    print(f"funcionarios {nome} ja existe")
  else:
    comandoSQL = f'INSERT INTO funcionarios (nome, cargo) values ("{nome}", "{cargo}")'
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Criado {nome} com sucesso")
  
def AlterarDB(id, cargo):
  comandoSQL = f"SELECT * FROM funcionarios"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  ids_existentes = [linha[0] for linha in resultado]
  if id in ids_existentes:
    comandoSQL = f'UPDATE funcionarios SET cargo = "{cargo}" where idfuncionarios = {id}'
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Alterado com sucesso")
  else:
    print("ID não encontrado")

def DeleteDB(id):
  comandoSQL = f"SELECT * FROM funcionarios"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  ids_existentes = [linha[0] for linha in resultado]
  if id in ids_existentes:
    comandoSQL = f'DELETE FROM funcionarios WHERE idfuncionarios = {id}'
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Deletado com sucesso")
  else:
    print("ID não encontrado")

def SearchDB(indice):
  if indice == 'nome':
    comandoSQL = f"SELECT * FROM funcionarios"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()  
    for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<10}")
  if indice == 'cargo':
    comandoSQL = f"SELECT * FROM funcionarios"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()  
    for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<10}")
  if indice not in ('nome', 'cargo'):
    print("indice nao encontrado")

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
    nome = input("nome: ")
    cargo = input("cargo: ")
    InsertDB(nome, cargo)
    
  if escolha == 2:
    id = int(input("id: "))
    cargo = input("cargo: ")
    AlterarDB(id, cargo)
    
  if escolha == 3:
    id = int(input("id: "))
    DeleteDB(id)
    
  if escolha == 4:
    indice = input("indice: ")
    SearchDB(indice)
    
  if escolha == 5:
    exit()