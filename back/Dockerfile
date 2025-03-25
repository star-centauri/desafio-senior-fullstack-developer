# Iamgem de instalação do python
FROM python:3.9

# pasta onde vai ficar o projeto
WORKDIR /app

# movimentação dos arquivos de instalação de depencias 
COPY ./requirements.txt /code/requirements.txt

# Instalação das dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Movimentação do restante do codigo
COPY . .

# Execução da API
CMD ["fastapi", "run", "main.py", "--port", "80"]