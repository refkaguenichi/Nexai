FROM node:20-bullseye

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

# 👇 force webpack, disable turbopack native css
ENV NEXT_DISABLE_TURBOPACK=1

RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start"]
