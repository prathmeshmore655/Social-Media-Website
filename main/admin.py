from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

class display_followers_table(admin.ModelAdmin):

    list_display = ('id','follower_name','follower_of_id','follower_of_username')


class display_comments(admin.ModelAdmin):

    list_display = ('id','comments','comment_By','time','post_id_id','by_commented')

class display_post(admin.ModelAdmin):

    list_display = ('id','post_file','caption','created_time','post_no_id','no_of_likes')

class display_reels(admin.ModelAdmin):

    list_display = ('id','reel_video','caption','uploaded_time','reels_no')



admin.site.register(Reels,display_reels)
admin.site.register(Post,display_post)
admin.site.register(Followers,display_followers_table)
admin.site.register(Comments,display_comments)