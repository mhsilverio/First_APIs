
FROM node:latest

WORKDIR /conf/routes

COPY package*.json ./

RUN npm install

COPY . .

CMD [ "npm", "start" ]
