from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=150)
    desc = models.TextField()
    body = models.TextField()   
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    img = models.ImageField(
        upload_to="images/",null = True, blank=True)

    def number_of_likes(self):
        return self.likes.count()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
   

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    body =models.TextField(max_length=110)
    name = models.CharField(max_length=20)
    date_added= models.DateTimeField(default=timezone.now)
   
  

    def  __str__(self):
        return '%s - %s'%(self.post.title , self.name)
        


class Profile(models.Model): 
	user = models.OneToOneField(User, on_delete=models.CASCADE)

