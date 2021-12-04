from celery import Celery

app = Celery('tasks', broker='redis://localhost:6382/0', backend='redis://localhost:6382/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
)


@app.task
def add(x, y):
    return x + y
