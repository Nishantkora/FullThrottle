# FullThrottle

FullThrottle is a web application for time period activities of user across different months.

## Setup

### Install virtual environment on ubuntu 18.04

mkdir .virtualenv
sudo apt install python3-pip
pip3 install virtualenv
pip3 install virtualenvwrapper
vim .bashrc

#### Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.
export WORKON_HOME=$HOME/.virtualenvs.
export VIRTUALENVWRAPPER_VIRTUALENV=/home/goran/.local/bin/virtualenv.
source ~/.local/bin/virtualenvwrapper.sh.

#### Restart the console to load virtualenvironment from bash

#### Create new virtual environment 
mkvirtualenv name_of_your_env

#### You should confirm that this environment is set up for Python3:
Python -V

#### To deactivate the environment use the deactivate command.:
deactivate

#### To list all available virtual environments use the command workon or lsvirtualenv (Same result as workon but shown in a fancy way) in your terminal:
workon
lsvirtualenv

#### To activate one specific environment use workon + name of your environment:
workon name_of_your_env

#### Once virtual Environment is created.
#### Go to specified directory to clone the project
git clone 

#### Install using pip
pip install -r requirements.txt


## Populate the data

### Move to the project folder and run the following command
python manage.py populate_data

## Run the project

### Move to the project folder and run the following command
python manage.py runserver

### To access the users activity oeriod across months through api and go to browser and type
http://localhost:8000/user/users
