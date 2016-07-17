from django.db import models


# Create your models here.
class Human(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Human(name={},x={},y={})".format(self.name, self.x, self.y)
