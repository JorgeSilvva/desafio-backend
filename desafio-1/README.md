### Importador de dados CSV para MySQL

O objetivo deste código é ler um arquivo CSV com informações de filmes e inserir ou atualizar essas informações em uma tabela no banco de dados MySQL.

### Funcionamento

O script lê as informações do arquivo CSV por meio da função read_csv_file() e retorna os dados como uma lista de listas. Em seguida,
a função insert_data_into_mysql_db() é chamada via "thread", usando o módulo "concurrent.futures". Essa função conecta-se ao banco de dados MySQL e
percorre as linhas da lista, estraindo o ID, título, ano e gêneros do filme. Em seguida, insere ou atualiza esses dados na tabela "movies" no banco de dados "filmes".
Se um registro com o mesmo ID já existir na tabela, os dados serão atualizados; caso contrário, um novo registro será inserido.

### Pré-requisitos

Antes de executar o script é necessário ter instalado:

* Python 3.x;
* As bibliotecas "concurrent.futures" e "mysql-connector-python";
* Um servidor MySQL em execução.

### Instalação das dependências

As dependências constam no arquivo ["requirements.txt"](https://github.com/JorgeSilvva/desafio-backend/blob/main/desafio-1/requirements.txt). Para instalá-las, basta executar o comando a seguir no terminal:

* pip install -r requirements.txt

### Implementação do Banco de Dados

Para implementar o banco de dados basta executar a query com o código SQL exposto no arquivo ["db.sql"](https://github.com/JorgeSilvva/desafio-backend/blob/main/desafio-1/requirements.txt), criando o banco de dados "filmes" e a tabela "movies".

### Como usar

* Certifique-se de que o arquivo "movie.csv" com os dados dos filmes esteja no mesmo diretório;
* Edite as informações de autenticação (user, password, host, database) para o banco de dados MySQL na função main();
* Abra um terminal e navegue até o diretório onde o script está salvo;
* Execute o comando python app.py para executar o script.
