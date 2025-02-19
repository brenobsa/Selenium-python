import os
import psycopg2
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do banco de dados
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'teste')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', '8800')

def connect_db():
    """Conecção ao banco de dados PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None

def insert_data(titulo, link, source):
    """Insere dados no banco de dados."""
    conn = connect_db()
    if conn is None:
        return  # Não prosseguir se a conexão falhar

    try:
        with conn.cursor() as cursor:
            table = f"noticias_{source}"
            cursor.execute("SELECT to_regclass(%s);", (table,))
            if cursor.fetchone()[0] is None:
                print(f'Tabela {table} não existe.')
                return
            if titulo and link:
                cursor.execute(f"INSERT INTO {table} (titulo, link) VALUES (%s, %s)", (titulo, link))
                conn.commit()
                print(f'Inserindo no banco: Titulo: {titulo} Link: {link} na tabela {source}')
            else:
                print("Título ou link não podem ser None.")

    except Exception as e:
        print(f'Erro ao inserir dados: {e}')
    finally:
        conn.close()




def scrape(url, title_selector, source):
    # Inicia um display virtual para rodar o Firefox sem interface gráfica
    display = Display(visible=0, size=(1024, 768))
    display.start()

    try:
        with webdriver.Firefox() as navegador:
            navegador.get(url)

            WebDriverWait(navegador, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, title_selector))
            )

            artigos = navegador.find_elements(By.CSS_SELECTOR, title_selector)

            for artigo in artigos:
                titulo = artigo.text
                link = artigo.get_attribute('href')
                print(f'Coletando Dados: Titulo `{titulo}, Link: {link}')
                if titulo and link:
                    insert_data(titulo, link, source)
                else:
                    print("Título ou link não encontrados.")

    finally:
        display.stop()

sites = [
    {'url': 'https://www.globo.com/', 'selector': 'a.post__link', 'source': 'globo'},
    {'url': 'https://techcrunch.com/', 'selector': 'a.loop-card__title-link', 'source': 'tech'}
]

for site in sites:
    scrape(site['url'], site['selector'], site['source'])
