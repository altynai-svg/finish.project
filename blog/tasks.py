from celery import shared_task

@shared_task
def sample_task():
    print("Задача выполнена успешно!")

