from django.db import models
class Cate(models.Model):
    category_name=models.CharField(max_length=50)
    category_des=models.TextField()
    def __str__(self) -> str:
        return self.category_name  

class Room(models.Model):
    room_no=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.room_no
    
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_des=models.CharField(max_length=50)
    product_quantity=models.IntegerField(default=1)
    room_no = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True,blank=False)
    category_name = models.ForeignKey(Cate, on_delete=models.SET_NULL,null=True,blank=False)
    def __str__(self) -> str:
        return self.product_name
    
class ProductMessage(models.Model):
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)






