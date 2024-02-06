from django.db import models


class File(models.Model):
    """Модель для загружаемых файлов."""

    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="downloads/", max_length=256)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

