from time import sleep

from celery import shared_task

@shared_task
def notify_customers(message):
    print('Notifying customers...')
    # Here you would implement the actual notification logic, e.g., sending emails.
    print(f'Notification sent with message: {message}')
    sleep(10)  # Simulate a time-consuming task
    print('Finished notifying customers.')
