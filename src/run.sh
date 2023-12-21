#!/bin/bash

#check if python is installed 
python3 --version


#check if venv exists
python3 -m venv .venv
#activate virtual environment
source .venv/bin/activate

#packages
pip3 install colored

#To use application
python3 src/main.py