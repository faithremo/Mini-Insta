from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.caption
    
class User(models.Model):
    username = models.CharField(max_length =30)
    email = models.EmailField()
    password = models.CharField(max_length =30)
    password2 = models.CharField(max_length =30)
    
    def __str__(self):
        return self.caption
    
    
class Likes(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagelikes')
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlikes')

    def __str__(self):
        return "%s like" % self.image
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    photo = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=255)
    
    def __str__(self):
        return "%s comment" % self.photo
    
    


class miniIG(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')