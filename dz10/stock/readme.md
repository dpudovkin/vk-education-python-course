# Instruction

## Celery
```shell
celery -A application worker -l INFO -B
```
## Flower
```shell
celery -A application flower --port=5555
```

## Django
```shell
./manage.py runserver
```
## Docker-compose
```shell
./manage.py runserver
```