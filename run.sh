#!/bin/bash
source .env/bin/activate
xfce4-terminal --geometry 80x20+200+200 -e "python3 main_server.py" &
xfce4-terminal --geometry 80x20+800+200 -e "python3 main_client.py" &
