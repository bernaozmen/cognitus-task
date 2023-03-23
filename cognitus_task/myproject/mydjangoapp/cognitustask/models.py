from django.db import models

# Create your models here.

class Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    label = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
