import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "hotel"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def CadastrarReserva(nome, quarto, data_entrada, data_saida):
  comandoSQL = f"SELECT * FROM reserva"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  quartosReservados = [linha[2] for linha in resultado]
  if quarto in quartosReservados:
    print("Quarto ja reservado")
  else:
    comandoSQL = f"INSERT into reserva(nomecliente, quarto, datacheckin, datacheckout) values('{nome}', '{quarto}', '{data_entrada}', '{data_saida}')"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print(f"Reserva efetuada com sucesso")
        
def AlterarReserva(id, datacheckin, datacheckout):
  comandoSQL = f"SELECT * FROM reserva"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids = [linha[0] for linha in resultado]
  if id in ids:
    comandoSQL = f"UPDATE reserva SET datacheckin = '{datacheckin}', datacheckout = '{datacheckout}' where idreserva = {id}"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print('Alterado com sucesso')
  else:
    print("ID não encontrado")

def ExcluirReserva(id): 
  comandoSQL = f"SELECT * FROM reserva"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  ids = [linha[0] for linha in resultado]
  if id in ids:
    comandoSQL = f"DELETE FROM reserva WHERE idreserva = {id}"
    cursor.execute(comandoSQL)
    DBconexao.commit()
    print('Deletado com sucesso')
  else:
    print("ID nao encontrado")
    
def ListarReservas():
  comandoSQL = f"SELECT * FROM reserva"
  cursor.execute(comandoSQL)
  resultado = cursor.fetchall()
  for i in resultado: print(f"{i[0]:<5}|{i[1]:<15}|{i[2]:<5}|{i[3]}|{i[4]}")

    
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
    quarto = input("Quarto: ")
    data_entrada = input("Data entrada: ")
    data_saida = input("Data saida: ")
    CadastrarReserva(nome, quarto, data_entrada, data_saida)
  
  if escolha == 2:
    id = int(input("ID: "))
    data_entrada = input("Data entrada: ")
    data_saida = input("Data saida: ")
    AlterarReserva(id, data_entrada, data_saida)
  
  if escolha == 3:
    id = int(input("ID: "))
    ExcluirReserva(id)
  
  if escolha == 4:
    ListarReservas()
  
  if escolha == 5:
    exit()