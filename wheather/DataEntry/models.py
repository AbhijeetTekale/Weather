from django.db import models

class Test(models.Model):
    parameter1 = models.CharField(max_length=10)
    parameter2 = models.CharField(max_length=10)
    parameter3 = models.CharField(max_length=10)
    parameter4 = models.CharField(max_length=10)
    parameter5 = models.CharField(max_length=10)
    parameter6 = models.CharField(max_length=10)
    parameter7 = models.CharField(max_length=10)
    parameter8 = models.CharField(max_length=10)
    Date       = models.DateField()
    Time       = models.TimeField()
    def __str__(self):
        return self.id