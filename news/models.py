from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField()
    image = models.ImageField(upload_to="news/")

    publish_date = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        return mark_safe(f"<img style='width:300px' src='{self.image.url}'>")

    def __str__(self):
        return f"{self.title}"
