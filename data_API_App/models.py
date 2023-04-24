from django.db import models

#######################################
class Data_base(models.Model):
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Shop(models.Model):
    snack = models.CharField(max_length=255)
    drink = models.CharField(max_length=255)
    def __str__(self):
        return self.snack

 