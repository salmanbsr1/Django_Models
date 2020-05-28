from django.db import models


# Create your models here.
class Destination:
    id = models.IntegerField(10)
    name: str
    desc: str
    image: str
    price: int
