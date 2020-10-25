#!/bin/bash
gunicorn_path=$(find /home/cast/.cache/pypoetry/virtualenvs -name "gunicorn" | grep -v lib)
cd /home/cast/site
${gunicorn_path} --access-logfile - --error-logfile - -b 127.0.0.1:8001 config.wsgi
