# Usa a imagem base do Ubuntu
FROM ubuntu:20.04

# Instala dependências necessárias
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    firefox \
    xvfb \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*



# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Comando para rodar o script com pyvirtualdisplay
CMD ["python3", "Scraping.py"]
