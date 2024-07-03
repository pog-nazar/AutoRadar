#!/bin/bash
echo "Starting bot"
python bot/main.py &

echo "Starting server"
python server.py