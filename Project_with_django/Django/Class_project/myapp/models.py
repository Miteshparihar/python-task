from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.IntegerField()
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='user/',default='user/person.png')
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name+"-"+self.user
    
class Category(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    

class Product(models.Model):
    farmer=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='plants')
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    p_img=models.ImageField(upload_to='images/')
    p_stock=models.IntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.pname+"-"+self.farmer.name
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=100)
    blog_img=models.ImageField(upload_to='blog_images/')
    desc= models.TextField()
    def __str__(self):
        return self.blog_title+' - '+self.user.name+f'({self.user.user})'
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    availability=models.BooleanField()
    payment_status=models.BooleanField(default=False)
    razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_signature=models.CharField(max_length=100,null=True,blank=True)

    total=models.IntegerField()
    date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.product.pname+ f"{self.payment_status}"+self.user.name
class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    grand_amount=models.IntegerField()
    trans_id=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateTimeField(default=timezone.now())
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.product.pname+"-"+self.user.name