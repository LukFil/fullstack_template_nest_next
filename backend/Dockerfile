FROM node:18-alpine AS development
    MAINTAINER Lukas Peter Filipcik <lukas.filipcik@octoshrew.com>

WORKDIR /usr/src/app
COPY package.json yarn.lock ./

RUN yarn install
COPY . .

# RUN yarn test:watchAll
# RUN yarn start:dev
RUN yarn build

# CMD ["yarn", "test:watchAll", "&&", "yarn", "start:dev"]

FROM node:18-alpine AS production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /usr/src/app
COPY package.json yarn.lock ./

RUN yarn install --production=true --frozen-lockfile
COPY . .
COPY --from=development /usr/src/app/dist ./dist

# RUN yarn build
# CMD ["node", "dist/main"]
