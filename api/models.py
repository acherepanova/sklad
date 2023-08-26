from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Sklad(models.Model):
    name = models.CharField(max_length=120)


class Tovar(models.Model):
    id_tov = models.IntegerField()
    sklad = models.ForeignKey(Sklad, related_name="tovars", on_delete=models.CASCADE)


class Posting(models.Model):
    tovar = models.ForeignKey(Tovar, related_name="postings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="postings", on_delete=models.CASCADE)
