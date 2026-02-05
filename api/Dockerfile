# 1️⃣ Use Node.js LTS Alpine
FROM node:20-alpine

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Install curl (needed for HEALTHCHECK)
RUN apk add --no-cache curl

# 4️⃣ Copy package.json and install dependencies
COPY package*.json ./
RUN npm install --production

# 5️⃣ Copy source code
COPY . .

# 6️⃣ Build NestJS app
RUN npm run build

# 7️⃣ Expose port (backend)
EXPOSE 5000

# 8️⃣ Healthcheck
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# 9️⃣ Start server
CMD ["npm", "run", "start"]
