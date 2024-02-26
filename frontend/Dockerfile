FROM node:16
WORKDIR /app
COPY ./bookstore/package.json .
COPY ./bookstore/package-lock.json .
RUN npm install
COPY ./bookstore .
CMD ["npm", "run", "serve"]
EXPOSE 8080
