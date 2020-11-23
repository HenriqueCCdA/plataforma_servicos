# Plataforma

## Ambiente Virtual e instalando requirements
```
    $ python3 -m venv plataforma_venv

    $ source plataforma_venv/bin/activate

    $ pip3 install --upgrade pip

    $ pip3 install -r requirements.txt
```

## Rodando a Aplicação e migrando para o BD:
``` 
    export FLASK_APP=application.py

    #migrando o BD
    $ flask db init

    $ flask db migrate

    $ flask db upgrade

    #rodando a aplicação:
    flask run
```
