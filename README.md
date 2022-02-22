# Quiz DevPro

Projeto "Quiz DevPro" é um jogo de perguntas e respostas desenvolvido em uma das edições da Jornada Rumo a Primeira Vaga do [Site Python Pro](https://www.python.pro.br) 

Projeto disponível em https://quiz-dev-pro.herokuapp.com/

[![Django CI](https://github.com/mateuslourenco/quizdevpro/actions/workflows/django.yml/badge.svg)](https://github.com/mateuslourenco/quizdevpro/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/mateuslourenco/quizdevpro/shield.svg)](https://pyup.io/repos/github/mateuslourenco/quizdevpro/)
[![Python 3](https://pyup.io/repos/github/mateuslourenco/quizdevpro/python-3-shield.svg)](https://pyup.io/repos/github/mateuslourenco/quizdevpro/)
[![codecov](https://codecov.io/gh/mateuslourenco/quizdevpro/branch/main/graph/badge.svg?token=87LLQ6QMFL)](https://codecov.io/gh/mateuslourenco/quizdevpro)


## Descrição
Neste projeto, foi desenvolvido um jogo perguntas e respostas. Ao responder uma pergunta, é calculado a pontuação obtida, após todas as perguntas serem respondidas, será exibido um ranking com as melhores pontuações

## Como rodar o projeto localmente

- Clone esse repositório
- Instale o pipenv 
- Instale as dependencias
- Copie as variáveis de ambiante
- Inicie o banco de dados postgres com docker
- Rode as migrações


```
git clone https://github.com/mateuslourenco/quizdevpro.git
cd quizdevpro
python -m pip install pipenv
pipenv sync -d
cp contrib/env-sample .env
docker-compose up -d
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

