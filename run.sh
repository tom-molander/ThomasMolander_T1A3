#!/bin/bash

#link to download python 3
download python 3 https://www.python.org/downloads/


#check if venv exists
python3 -m venv .todo-venv
#activate virtual environment
source .todo-venv/bin/activate

#packages
pip3 install colored

#To use application
python3 main.py