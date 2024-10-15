import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "escola"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def CadastrarAluno(nome, curso, anoingressao):
    comandoSQL = "SELECT nome, curso FROM alunos"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    alunos_registrados = [(linha[0], linha[1]) for linha in resultado]
    if (nome, curso) in alunos_registrados:
        print('Aluno com esse curso já existe')
    else:
      comandoSQL = f'INSERT INTO alunos(nome, curso, ano) values("{nome}", "{curso}", {anoingressao})'
      cursor.execute(comandoSQL)
      DBconexao.commit()
      print('Cadastrado com sucesso')

def AlterarAluno(id, indice, novoindice):
  comandoSQL = "SELECT * from alunos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids = [linha[0] for linha in resultado]
  if id in ids:
    if indice == 'curso':
      comandoSQL = f"UPDATE alunos SET curso = '{novoindice}' where idalunos = {id}"
      cursor.execute(comandoSQL)
      DBconexao.commit()
      print("Alterado com sucesso!")
    elif indice == 'ano':
      valor = int(novoindice)
      comandoSQL= f"UPDATE alunos SET ano = {valor} where idalunos = {id}"
      cursor.execute(comandoSQL)
      DBconexao.commit()
      print("Alterado com sucesso!")
    else: 
      print('indice nao encontrado')
  else:
    print('id nao encontrado')
    
def ExcluirAluno(id): 
  comandoSQL = f"SELECT * FROM alunos"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids = [linha[0] for linha in resultado]
  if id in ids:
    comandoSQL = f"DELETE FROM alunos WHERE idalunos = {id}"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print('Deletado com sucesso')
  else:
    print("ID nao encontrado")
  
def PesquisarAluno(indice, valor):
  if indice == 'ano':
    comandoSQL = f"SELECT * from alunos WHERE ano = {valor}"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<5}|{i[3]}")
  elif indice == 'curso':
    comandoSQL = f"SELECT * from alunos WHERE curso = '{valor}'"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<5}|{i[3]}")
  else:
    print('indice nao encontrado')
  
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
    curso = input("Curso: ")
    ano = int(input("Ano de ingresso: "))
    CadastrarAluno(nome, curso, ano)
  if escolha == 2:
    id = int(input('ID: '))
    indice = input('Indice [ano/curso]: ')
    novoindice = input('valor: ')
    AlterarAluno(id, indice, novoindice)
  if escolha == 3:
    id = int(input('ID: '))
    ExcluirAluno(id)
  if escolha == 4:
    indice = input('indice: ')
    valor = input('valor: ')
    PesquisarAluno(indice, valor)
  if escolha == 5:
    exit()