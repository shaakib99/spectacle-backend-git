from django.db import models

class Product(models.Model):
    colorChoices = [
        ('black', 'black'),
        ('blue', 'blue')
    ]
    product_id = models.IntegerField(primary_key = True,unique = True, auto_created = True)
    title = models.CharField(max_length = 256, blank = False, null = False, db_index = True)
    country = models.CharField(max_length = 256, blank = False, null = False)
    price = models.FloatField(null = False, blank = False)
    colors = models.CharField(choices=colorChoices, max_length = 256)
    image = models.CharField(max_length=256, blank = False, null = False)
