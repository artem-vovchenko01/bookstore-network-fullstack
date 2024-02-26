FROM node:16
WORKDIR /app
COPY ./bookstore .
RUN npm install
CMD ["npm", "run", "serve"]
EXPOSE 8080
