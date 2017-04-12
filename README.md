# Atmosphere
Project for photostudio "Atmosphere" by Tixxxon and fenixsarov

# Installation environment
Install Python 3.6 from http://www.python.org/
Install pip3 for Python
Install virtualenv and virtualenvwrapper
'''
    >pip3 isntall virtualenv
    >pip3 isntall virtualenvwrapper
'''

For Ubuntu:
Add to ./bashrc or execute each time before starup OS
'''
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
'''

Install Nodejs from https://www.npmjs.com/get-npm
Install lessc
'''
>npm install less -g
'''
Add to PATH path to lessc, example
/home/nodejs/node_modules/less/bin

Create new virtualenv and run this
'''
>mkvirtualenv Atmosphere_env
>workon Atmosphere_env
'''
Run this command for instal requiremnt python modules
'''
>pip3 install -r requirements.txt
'''

Create Atmosphere directory and clone this repository
'''
>mkdir Atmosphere
>cd Atmosphere
>git clone https://github.com/fenixsarov/Atmosphere
'''

# Optional
For development and debuging use SQLite by Django
For realese install MySQL from https://www.mysql.com/

# Run project
'''
>workon Atmosphere_env
>python3 manage.py migrate
>python3 manage.py runserver 8000
'''

Open http://127.0.0.1:8000 in your browser