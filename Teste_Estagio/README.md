# Teste Estagio de TI


Criar um script Python que utilize Selenium para coletar dados de uma página web e armazená-los em um
banco de dados PostgreSQL, rodando tudo dentro de um container Docker com docker-compose .

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto
/Teste_Estagio


├── create_table.sql
- Script SQL para criar as tabelas no banco de dados

├── docker-compose.yml        
- Configuração dos serviços Docker

├── Dockerfile                
- Instruções para construir a imagem do Docker

├── README.md                 
- Documentação do projeto

├── Requirements.txt          
- Dependências do Python

├── Scraping.py               
- Script principal para coletar dados


## Configuração do Ambiente

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   
2. **Instale as dependências:**
    ```
    pip install -r requirements.txt

## Executando o Projeto

1. **Inicie os contêineres:**
Use o Docker Compose para iniciar os contêineres:
    ```bash
    docker-compose up --build

2. **Acesso ao banco de dados e criação das Tabelas:**

- Para acessar o banco de dados PostgreSQL, use o seguinte comando:
    ```bash
    docker exec -it teste_estagio-db-1 psql -U postgres -d teste

- Para executar a Criação das tabelas:
    ```bash 
    \i /app/create_table.sql

3. **Executar o Script de Coleta de Dados**:
    ```bash
    docker-compose run app python3.8 /app/Scraping.py