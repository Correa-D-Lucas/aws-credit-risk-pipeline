FROM python:3.11-slim

# Instala dependências do sistema (Java + Git + utilitários)
RUN apt-get update && \
    apt-get install -y \
    default-jdk \
    git \
    curl \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Define diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala bibliotecas Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto inteiro
COPY . .

# Comando padrão (pode mudar depois)
CMD ["python3"]