#!/bin/bash
gunicorn_path=$(find /home/cast/.cache/pypoetry/virtualenvs -name "gunicorn" | grep -v lib)
${gunicorn_path} -b :8001 config.wsgi
