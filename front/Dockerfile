# Utilizar a imagem Node mais recente
FROM node:lts-alpine

# A pasta que vai ficar a aplicação
WORKDIR /app

# Copia somente package.json primeiro para a pasta app
COPY package.json .

# instalação das dependencias
RUN npm install

# Copia o restante do código
COPY . .

# Porta de acesso para a aplicação se executada
EXPOSE 3000

# Comando executado depois de terminar todo o processo de instalação do projeto
CMD ["npm", "run", "dev"]