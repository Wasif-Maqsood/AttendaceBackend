#!/bin/bash

cd /home/wise/New/backend
source /home/wise/anaconda3/bin/activate attendance
python manage.py runserver 0.0.0.0:8000
