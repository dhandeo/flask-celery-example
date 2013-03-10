from celery import Celery, current_task
from time import sleep

celery = Celery(broker="mongodb://127.0.0.1/celery", backend="mongodb://127.0.0.1/celery")

@celery.task(name="tasks.add")
def add(x, y):
    print "Starting job ..", x, y
    for i in range(x):
        sleep(1)
        current_task.update_state(state='PROGRESS', meta=str({'current': i, 'total': x}))
    return y

if __name__ == "__main__":
    celery.start()
