FROM node:latest

WORKDIR /app

COPY packjson.json .

RUN npm install

COPY . ./

EXPOSE 21262

CMD ["npm", "start"]