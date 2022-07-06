FROM node:18-alpine AS development
    MAINTAINER Lukas Peter Filipcik <lukas.filipcik@octoshrew.com>

WORKDIR /app

# Copy lock files if file exists
COPY package.json yarn.lock* package-lock.json* .

RUN yarn install

COPY . .
ENV NEXT_TELEMETRY_DISABLED 1

CMD yarn dev
