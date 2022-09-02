from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = "Category"

class Gym(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.FloatField(default=300)
    description = models.CharField(max_length=1000)
    imageurl = models.ImageField(upload_to = "Images",default='abc.jpg')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)

    def __str__(self):
        return self.service_name


    class Meta:
        db_table = "Gym"




