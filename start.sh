#!/bin/bash
echo "Starting bot"
python bot/main.py &

echo "Starting Flask server with Gunicorn"
gunicorn server:app -b 0.0.0.0:$PORT
