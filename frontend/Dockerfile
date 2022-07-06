FROM node:18-alpine AS development
    MAINTAINER Lukas Peter Filipcik <lukas.filipcik@octoshrew.com>

RUN apk add --no-cache libc6-compat

WORKDIR /usr/src/app
COPY package.json yarn.lock ./

RUN yarn install
COPY . .

ENV NEXT_TELEMETRY_DISABLED 1

RUN yarn next build

FROM node:18-alpine AS production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
ENV NEXT_TELEMETRY_DISABLED 1

RUN apk add --no-cache libc6-compat

WORKDIR /usr/src/dep

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs

COPY --from=development  /usr/src/app/public ./public
COPY --from=development  /usr/src/app/next.config.js .
COPY --from=development  /usr/src/app/package.json .
COPY --from=development  /usr/src/app/yarn.lock .

# COPY --from=development --chown=nextjs:nodejs /usr/src/app/.next/standalone ./
# COPY --from=development --chown=nextjs:nodejs /usr/src/app/.next/static ./.next/static
COPY --from=development --chown=nextjs:nodejs /usr/src/app/.next/standalone ./
COPY --from=development --chown=nextjs:nodejs /usr/src/app/.next/static ./.next/static

RUN ls -la

# CMD ["node", "server.js"]
