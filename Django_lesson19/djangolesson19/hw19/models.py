from django.db import models


class Aviaticket(models.Model):
    name = models.CharField(max_length=50)
    from_him = models.CharField(max_length=50)
    where_him = models.CharField(max_length=50)
    what = models.IntegerField()
    date = models.DateTimeField(auto_now=False)


