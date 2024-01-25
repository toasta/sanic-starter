#! /bin/bash

python3 -m venv venv
venv/bin/pip install -r requirements.txt

sanic server:app --debug
