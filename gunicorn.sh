#!/bin/bash
gunicorn_path=$(find /home/cast/.cache/pypoetry/virtualenvs -name "gunicorn" | grep -v lib)
cd /home/cast/site
${gunicorn_path} -b 127.0.0.1:8001 config.wsgi
