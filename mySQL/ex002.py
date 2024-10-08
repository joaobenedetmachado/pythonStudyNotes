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
  comandoSQL = f"SELECT * FROM empresa"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()  
  nomes_existentes = [linha[1] for linha in resultado]
  cargos_existentes = [linha[2] for linha in resultado] 
  if nome in nomes_existentes and cargo in cargos_existentes:
    print(f"funcionario {nome} ja existe")
  else:
    comandoSQL = f'INSERT INTO funcionario (nome, cargo) values ("nome", "cargo")'
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Criado {nome} com sucesso")