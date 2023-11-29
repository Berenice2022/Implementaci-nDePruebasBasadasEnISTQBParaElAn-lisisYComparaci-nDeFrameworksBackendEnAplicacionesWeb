from django.db import models

# Create your models here.
class User(models.Model):
    id= models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, verbose_name='UserName')
    email = models.EmailField(max_length=100, blank=True, verbose_name='Email')
    password = models.CharField(max_length=20, blank=True, verbose_name='Password')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Post(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False, default='', verbose_name='Description')
    #photo = models.CharField(max_length=1000, blank=False, default='')
    photo = models.ImageField(upload_to='images/', verbose_name='Photo Post', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

# TO LOOK THAT DATA WANT TO SEE ON THE ADMIN PANEL
    def __str__(self):
        return self.description

    def delete(self, using=None, keep_parents=False):
        self.photo.delete(self.photo.name)
        super().delete()


class Like(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=False, default='', verbose_name='Comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Event(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, default='', verbose_name='Name')
    description = models.CharField(max_length=200, blank=False, default='',verbose_name='Description')
    address = models.CharField(max_length=150, blank=False, default='', verbose_name='Address')
    #photography = models.CharField(max_length=1000, blank=False, default='',verbose_name='Photography')
    photography = models.ImageField(upload_to='images/', verbose_name='Photography',blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

class Interest(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_category = models.CharField(
        max_length=200, blank=False, default='', verbose_name='Category')
    name = models.CharField(max_length=100, blank=False, default='', verbose_name='Name')
    description = models.CharField(max_length=200, blank=False, default='', verbose_name='Description')
    importance = models.CharField(max_length=200, blank=False, default='', verbose_name='Importance')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

