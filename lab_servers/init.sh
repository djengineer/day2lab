#!/bin/bash
apt install zaproxy steghide docker.io docker-compose -y
systemctl enable docker --now
pip install flask requests
docker-compose -f ./mutillidae-docker/docker-compose.yml up --build -d
reboot






