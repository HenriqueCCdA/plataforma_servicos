# Plataforma de Serviços

![GitHub last commit](https://img.shields.io/github/last-commit/JuniorJDS/plataforma_servicos?style=plastic) ![GitHub](https://img.shields.io/github/license/JuniorJDS/plataforma_servicos?style=plastic) 

Esse projeto é uma estrutura básica para uma plataforma de Serviços com área do usuário, podendo ser feita requisição de serviços e envio de arquivos, e uma área do administrador que responderá as requisições.





## Ambiente Virtual e instalando requirements
```
    $ python3 -m venv venv

    $ source venv/bin/activate

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
