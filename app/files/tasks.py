from celery import shared_task
import time

from .models import File


@shared_task
def process_file(file_id: str) -> None:
    """Функция обработки файла."""

    file = File.objects.get(id=file_id)
    # Обработка файла
    time.sleep(10)
    file.processed = True
    file.save()