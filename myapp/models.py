from django.db import models

# Create your models here.
class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()

class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)

class employee(models.Model):
    employee_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    address=models.TextField()
    date_of_birth=models.DateField()

class blogmodel(models.Model):
    title=models.CharField(max_length=800)
    content=models.TextField()
    author=models.CharField(max_length=500)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class user_pro(models.Model):
    user_id=models.IntegerField(primary_key=True)
    User_name=models.CharField(max_length=100)
class product_use(models.Model):
    pro_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    user=models.ForeignKey(user_pro,on_delete=models.CASCADE)

class Organizer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    def __str__(self):
        return self.name
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=255)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
class Product_cate(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    stock_quantity=models.IntegerField()
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    rating=models.FloatField()
    description=models.CharField(max_length=100)
    def _str_(self):
        return self.name
class Booking(models.Model):
    guest_name=models.CharField(max_length=100)
    check_in_date=models.DateField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    def _str_(self):
        return self.guest_name
    
class user10(models.Model):
    user_name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone_number=models.CharField(max_length=100)

class userProfile(models.Model):
    username=models.CharField(max_length=150,unique=True)
    date_of_birth=models.DateField()
    location=models.CharField(max_length=100)
    bio=models.CharField(max_length=200)

class Post1(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class UserRegistration(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)

class Image(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    
