import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "biblioteca"

DBconexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

cursor = DBconexao.cursor()

def CadastrarLivro(titulo, autor, ano_publicacao, disponivel):
    comandoSQL = "SELECT titulo, autor FROM livros"
    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()
    livros_registrados = [(linha[0], linha[1]) for linha in resultado]

    if (titulo, autor) in livros_registrados:
        print('Livro já existe no banco de dados')
    else:
        comandoSQL = f'INSERT INTO livros(titulo, autor, ano_publicacao, disponivel) values("{titulo}", "{autor}", {ano_publicacao}, {disponivel})'
        cursor.execute(comandoSQL)
        DBconexao.commit()
        print('Livro cadastrado com sucesso')

def AlterarDisponibilidade(id):
    comandoSQL = "SELECT disponivel FROM livros WHERE id = %s"
    cursor.execute(comandoSQL, (id,))
    resultado = cursor.fetchone()

    if resultado:
        novo_status = not resultado[0] 
        comandoSQL = "UPDATE livros SET disponivel = %s WHERE id = %s"
        cursor.execute(comandoSQL, (novo_status, id))
        DBconexao.commit()
        status_texto = "disponível" if novo_status else "não disponível"
        print(f"Status do livro alterado para {status_texto}")
    else:
        print("ID do livro não encontrado")

def ExcluirLivro(id):
    comandoSQL = "SELECT * FROM livros WHERE id = %s"
    cursor.execute(comandoSQL, (id,))
    resultado = cursor.fetchone()

    if resultado:
        comandoSQL = "DELETE FROM livros WHERE id = %s"
        cursor.execute(comandoSQL, (id,))
        DBconexao.commit()
        print('Livro excluído com sucesso')
    else:
        print("ID do livro não encontrado")

def PesquisarLivro(indice, valor):
    if indice == 'titulo':
        comandoSQL = f"SELECT * FROM livros WHERE titulo LIKE '%{valor}%'"
    elif indice == 'autor':
        comandoSQL = f"SELECT * FROM livros WHERE autor LIKE '%{valor}%'"
    else:
        print('Índice não encontrado')
        return

    cursor.execute(comandoSQL)
    resultado = cursor.fetchall()

    if resultado:
        for livro in resultado:
            disponivel_texto = "Sim" if livro[4] else "Não"
            print(f"{livro[0]:<5}| {livro[1]:<30}| {livro[2]:<20}| {livro[3]:<5}| Disponível: {disponivel_texto}")
    else:
        print("Nenhum livro encontrado")

while True:
    print("""
        (1) - Cadastrar Livro
        (2) - Alterar Status de Disponibilidade
        (3) - Excluir Livro
        (4) - Pesquisar Livro
        (5) - Sair
    """)

    escolha = int(input("> "))

    if escolha == 1:
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = int(input("Ano de Publicação: "))
        disponivel = int(input("Disponível [1 para Sim, 0 para Não]: "))
        CadastrarLivro(titulo, autor, ano_publicacao, disponivel)

    elif escolha == 2:
        id = int(input('ID do livro: '))
        AlterarDisponibilidade(id)

    elif escolha == 3:
        id = int(input('ID do livro: '))
        ExcluirLivro(id)

    elif escolha == 4:
        indice = input('Pesquisar por [titulo/autor]: ')
        valor = input(f'Valor da pesquisa (nome do {indice}): ')
        PesquisarLivro(indice, valor)

    elif escolha == 5:
        print("Encerrando o programa.")
        break
