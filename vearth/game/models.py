from composite_field import CompositeField
from django.db import models

class CoordField(CompositeField):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return "Coord(x={},y={})".format(self.x, self.y)


# Create your models here.
class Human(models.Model):
    coord = CoordField();
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Human(name={},coord={})".format(self.name, self.coord)
