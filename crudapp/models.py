from django.db import models

# Create your models here.
class Crud(models.Model):
    si = models.IntegerField()
    item = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.si)