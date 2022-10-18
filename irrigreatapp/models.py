from django.db import models
from datetime import datetime

# Create your models here.
class SmUser(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20 ,unique=True)
    password = models.CharField(max_length=20)
    bdate = models.DateTimeField(blank=True)
    gender = models.CharField(max_length=20)
    creatDate = models.DateTimeField(blank=True)
    updateDate = models.DateTimeField(blank=True)

class SmUserProfile(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(SmUser, related_name="smusers" ,on_delete= models.CASCADE)
    fname = models.CharField(max_length=20 ,default='Ferb')
    lname = models.CharField(max_length=20,default='Fletcher')
    email = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,blank=True)
    bdate = models.DateTimeField(max_length=20,blank=True)
    gender = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    userType = models.CharField(max_length=20 ,blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'irrigreatapp/images',default='irrigreatapp/images/defaultimg.png')
    follow = models.ManyToManyField(SmUser, related_name='follower')
    creatDate = models.DateTimeField( blank=True)
    updateDate = models.DateTimeField( blank=True)

    def total_follow(self):
        return self.follow.count()



class Post(models.Model):
    user_id = models.ForeignKey(SmUserProfile, related_name="Blogger" ,on_delete= models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to = 'irrigreatapp/images',blank=True)
    likes = models.ManyToManyField(SmUserProfile, related_name='likes')
    creatDate = models.DateTimeField( blank=True)
    updateDate = models.DateTimeField( blank=True)
    def total_like(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete= models.CASCADE)
    blogger_id = models.ForeignKey(SmUserProfile, related_name="bloggers" ,on_delete= models.CASCADE)
    commenter_id = models.ForeignKey(SmUserProfile, related_name="commenters" ,on_delete= models.CASCADE)
    parent = models.ForeignKey('self' ,related_name="parents", on_delete= models.CASCADE,null=True)
    body = models.TextField()
    creatDate = models.DateTimeField(blank=True, auto_now_add = True)
    updateDate = models.DateTimeField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.commenter_id)

    def total_comment(self):
        return self.body.count()
