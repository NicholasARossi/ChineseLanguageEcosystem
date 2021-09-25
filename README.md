# ChineseLanguageEcosystem
a set of web-apps and database infrastructure meant to interact with tinghaole

# notes for getting started with any new django app
* ```conda create --name django_ml python=3.8```
* ``` python -m pip install django```
*  ``` python -m django startproject core .```

# Notes for running docker
* ```docker build --tag ChineseEcosystem .```
* ```docker run --publish 8000:8000 ChineseEcosystem```