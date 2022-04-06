import profile
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = CloudinaryField()
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod    
    def all_posts(self):
        posts= Post.objects.all()
        return posts
    
    @classmethod    
    def search_user(self, username):
        user= User.objects.filter(username=username).first()
        return user
   

    
    def __str__(self):
        return self.caption
    
class Profile(models.Model):
    profile = CloudinaryField('profile-pic')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    bio = models.TextField(max_length=400,blank=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.user
    
    
class Likes(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagelikes')
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlikes')
    
    def save_likes(self):
        self.save()
        
    def delete_likes(self):
        self.delete()

    def __str__(self):
        return "%s like" % self.image
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    photo = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=255)
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
    
    def __str__(self):
        return "%s comment" % self.photo
    
    



