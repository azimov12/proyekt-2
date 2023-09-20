from django.db import models

# Create your models here.
class Noutbook(models.Model):
    noutbook_name = models.CharField(default="")
    information = models.TextField()
    price = models.SmallIntegerField(default=400)
    
    def __str__(self) -> str:
        return self.tittle