from django.db import models

# Create your models here.
class shoes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    descriptionShoes = models.TextField(max_length=150,default="pendiente")
    priceShoes = models.FloatField(null=True)
    fecha_publicacion = models.DateField()
    # imageShoes = models.ImageField(upload_to='Images/imageShoes', default="*")

