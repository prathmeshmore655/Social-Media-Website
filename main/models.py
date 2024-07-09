from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(default="Tell Something About You", blank=True)
    profile_picture = models.FileField(upload_to="profile_pictures/", default="profile_pictures/default.jpg")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username if self.user else 'Anonymous'




class Post(models.Model):
    post_no = models.ForeignKey(User, on_delete=models.CASCADE)
    post_file = models.FileField(upload_to="posts/")  
    caption = models.CharField(max_length=100, default="No caption yet")
    created_time = models.DateTimeField(auto_now_add=True)  
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    no_of_likes = models.IntegerField(default=0)

    
    
    def total_likes(self):
        return self.likes.count()

 
    


class Comments(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments_model")
    comments = models.CharField(max_length=255)    
    time = models.DateTimeField(auto_now_add=True)
    comment_By = models.CharField(max_length=10,default='Null')
    by_commented = models.CharField(max_length=50,default='NUll')
    
    def __str__(self):
        return self.comments


class Reply_Comments(models.Model):

    reply_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    reply = models.CharField(max_length=255)



class Followers(models.Model):
    follower_of = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower_id')
    follower_name = models.CharField(max_length=50)
    follower_of_username = models.CharField(max_length = 20, default='Null')

    



class Following(models.Model):

    following_no = models.ForeignKey(UserProfile,on_delete= models.CASCADE,related_name= "following_id")
    following_name = models.CharField(max_length=50)



class Reels(models.Model):

    reels_no = models.ForeignKey(User,on_delete=models.CASCADE)
    reel_video = models.FileField(upload_to='reels/')
    caption = models.CharField(max_length=50)
    uploaded_time = models.DateTimeField(auto_now_add= True)


