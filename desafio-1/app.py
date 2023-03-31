import concurrent.futures
import mysql.connector
import csv
import os
import re


# Função para ler o arquivo CSV e retornar as informações como uma lista de listas


def read_csv_file(file_path):
    try:
        # Abre o arquivo CSV no modo leitura ('r') e codificado em UTF-8
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            # Cria um objeto csv_reader para ler o conteúdo do arquivo CSV
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Pula a primeira linha do CSV, que contém o cabeçalho
            next(csv_reader)
            # Retorna a lista de dados obtidas no arquivo CSV
            return [row for row in csv_reader]
    except Exception as e:
        # Se ocorrer algum erro na leitura do arquivo CSV, imprime o erro e retorna None
        print(f'Erro ao ler o arquivo CSV: {e}')
        return None


# Função para inserir os dados no banco de dados MySQL


def insert_data_into_mysql_db(data, user, password, host, database):
    try:
        # Cria a conexão e um cursor usando um gerenciador de contexto
        with mysql.connector.connect(
                user=user, password=password, host=host, database=database) as conn, conn.cursor() as cursor:
            # Promove a iteração sobre cada linha dos dados
            for row in data:
                # Extrai o ID, título, ano e gêneros do filme
                id = int(row[0])
                title_and_year = row[1]
                year_matches = re.findall(r'\((\d+)\)', title_and_year)
                if year_matches:
                    year = int(year_matches[-1])
                    title = title_and_year[:title_and_year.rfind('(')].strip()
                    genres = row[2].split(',')
                else:
                    year = 0
                    title = title_and_year.strip()
                    genres = row[2].split(',')

                # Verifica se o ID do filme já existe na tabela "movies"
                query = "SELECT id FROM movies WHERE id = %s"
                cursor.execute(query, (id,))
                result = cursor.fetchone()

                if result:
                    # Atualiza o registro existente
                    update_query = "UPDATE movies SET title = %s, year = %s, genres = %s WHERE id = %s"
                    update_data = (title, year, ','.join(genres), id)
                    cursor.execute(update_query, update_data)
                    print(
                        f"O registro {id} foi atualizado na tabela 'movies'.")
                else:
                    # Insere um novo registro
                    insert_query = "INSERT INTO movies (id, title, year, genres) VALUES (%s, %s, %s, %s)"
                    insert_data = (id, title, year, ','.join(genres))
                    cursor.execute(insert_query, insert_data)
                    print(f"O registro {id} foi inserido na tabela 'movies'.")

            # Confirma as alterações na base de dados
            conn.commit()
            print(
                f"{len(data)} registros foram inseridos/atualizados na tabela 'movies'.")

    except mysql.connector.Error as e:
        # Lida com erros específicos do MySQL
        print(f"Erro {e.errno}: {e.msg}")
        conn.rollback()

    except Exception as e:
        # Lida com outros erros
        print(f"Erro: {e}")
        conn.rollback()


# Função principal


def main():
    # Define o caminho do arquivo CSV
    file_path = 'movie.csv'

    # Verifica se o caminho do arquivo é válido
    if not os.path.isfile(file_path):
        os.system("cls")
        print(
            f'\n Erro: O arquivo "{file_path}" deve estar no mesmo diretório do programa!')
        return

    # Lê o arquivo CSV e retorna uma lista de listas contendo os dados do arquivo
    data = read_csv_file(file_path)

    # Define as informações de autenticação para conectar ao banco de dados MySQL
    user = 'root'  # Especifice seu usuario
    password = 'root@2022'  # Especifique a sua senha
    host = 'localhost'  # Especifique o seu host
    database = 'filmes'  # Mesmo nome usado em db.sql

    # Divide a lista de dados em 4 pedaços para processá-los em paralelo
    chunk_size = len(data) // 4
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Cria um conjunto de threads para processar cada pedaço em paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for chunk in chunks:
            # Submete cada pedaço para ser inserido no banco de dados em uma thread separada
            futures.append(executor.submit(
                insert_data_into_mysql_db, chunk, user, password, host, database))

        # Espera todas as threads terminarem antes de encerrar o programa
        concurrent.futures.wait(futures)


# Função Menu


def menu():
    # loop principal para exibir o menu e processar a escolha do usuário
    while True:
        # exibe as opções do menu na tela
        print('''
            MENU:

            [L] - Ler o arquivo "movie.csv"
            [S] - Sair

        ''')

        # lê a escolha do usuário e converte para letras maiúsculas
        opcao = input('Escolha uma opção: ').upper()

        # verifica a escolha do usuário e chama a função adequada
        if opcao == 'L':
            main()
        elif opcao == 'S':
            print('Saindo...')
            # encerra o loop e sai da função
            break
        else:
            # opção inválida, exibe mensagem de erro e volta para o início do loop
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    # chama a função 'menu()' para iniciar o programa
    menu()
