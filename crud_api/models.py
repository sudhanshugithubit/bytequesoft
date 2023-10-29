from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Items(models.Model):
    id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=80)
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    finalprice=models.FloatField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock=models.BooleanField(default=True)
    description=models.TextField()


    def __str__(self):
        return self.item_name

