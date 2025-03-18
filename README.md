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
   git clone git@github.com:brenobsa/Selenium-python.git
   cd Selenium-python/Teste_Estagio
2. **Acessando a Pasta:**
   Primeiro, verifique o diretório atual em que você está localizado usando o comando pwd. Em seguida, liste os arquivos e pastas presentes no diretório com o comando ls para garantir que você está no caminho correto. Após confirmar que a pasta Teste_Estagio está presente, acesse-a utilizando o comando cd:
    ```
    pwd
    ls
    cd Teste_Estagio 
3. **Instale as dependências:**
    ```
    pip install -r requirements.txt

## Executando o Projeto

1. **Inicie os contêineres:**
Use o Docker Compose para iniciar os contêineres:
    ```bash
    docker-compose up --build #Executando a aplicação
    docker-compose up --no-start #Sem inicializar a aplicação

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
