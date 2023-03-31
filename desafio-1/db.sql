-- Cria o banco de dados 'filmes'

CREATE DATABASE filmes;

-- Usa o banco de dados 'filmes'

USE filmes;

-- Cria a tabela 'movies'

CREATE TABLE movies (
   id INT NOT NULL,
   title VARCHAR(255) NOT NULL,
   year INT NOT NULL,
   genres VARCHAR(255) NOT NULL,
   PRIMARY KEY (id)
);
