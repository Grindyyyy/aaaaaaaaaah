from celery import shared_task

@shared_task
def sharedtask(x,y):
    return x + y