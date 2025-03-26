# Iamgem de instalação do python
FROM python:3.9

# pasta onde vai ficar o projeto
WORKDIR /app

# movimentação dos arquivos de instalação de depencias 
COPY ./requirements.txt .

# Instalação das dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Movimentação do restante do codigo
COPY . .

# Expõe a porta
EXPOSE 8000

# Execução da API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]