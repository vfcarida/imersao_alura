# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependência e build
COPY pyproject.toml requirements.txt ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

# Copia o restante do código-fonte
COPY . .

# Expõe a porta que o Streamlit usa
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
