from django.db import models

# Create your models here.
class Noutbook(models.Model):
    noutbook_name = models.CharField(max_length=25, default="")
    information = models.TextField()
    price = models.SmallIntegerField(default=400)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.tittle