# Stage 1: Build React App
FROM node:20 AS builder

WORKDIR /app/frontend

COPY package.json ./
COPY package-lock.json ./
RUN npm install

# 필요한 소스 코드와 public 폴더만 복사
COPY frontend/public ./public
COPY frontend/src ./src

RUN npm run build

# Stage 2: Serve React App
FROM nginx:alpine

COPY --from=builder /app/frontend/build /usr/share/nginx/html

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
