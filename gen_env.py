#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Arguments to create unified .env file")

parser.add_argument(
    "env", metavar="Environment", type=str, help="ENV: production | development"
)

args = parser.parse_args()
env = args.env

if env == "production":
    out_env = open(".env", "w")
    out = "ENV_VAR=.env.production \n"
    out_env.write(out)
    frontend_env = open("./frontend/.env.production", "r")
    out_env.write(frontend_env.read())
    backend_env = open("./backend/.env.production", "r")
    out_env.write(backend_env.read())

elif env == "development":
    out_env = open(".env", "w")
    out = "ENV_VAR=.env \n"
    out_env.write(out)
    frontend_env = open("./frontend/.env", "r")
    out_env.write(frontend_env.read())
    backend_env = open("./backend/.env", "r")
    out_env.write(backend_env.read())
