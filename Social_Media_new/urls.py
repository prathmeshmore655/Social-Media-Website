
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home),
    path('create_user',views.user,name = "user"),
    path('login',views.Userlogin,name = "Userlogin"),
    path('profile_display',views.display_profile),
    path('update_profile',views.update_profile,name= "update_profile"),
    path('save_posts',views.save_post,name = "save_posts"),
    path('delete_post',views.delete_post, name = "delete_post")   ,
    path('Social_Media',views.social_media, name = "Social_Media"),
    path('profile',views.profile_sub,name = "profile_sub"),
    path('search',views.search_page,name="search"),
    path('reels',views.reels_page,name="reels"),
    path('LogOut',LogoutView.as_view(next_page = 'Userlogin'), name="logout"),
    path('post_comments',views.post_comments,name = "post_comments"),
    path('follow',views.follow, name = "follow"),
    path('unfollow',views.unfollow , name = "unfollow"),
    path('visit_profile',views.visit_profile, name ="visit_profile"),
    path('view_comments',views.view_comments, name = "view_comments"),
    path('like',views.like,name = "like"),
    path('get_comments/<int:post_id>/', views.get_comments, name='get_comments'),
    path('search_action',views.search_action, name="search_action"),
    path('upload_reel',views.upload_reel,name ="upload_reel"),
    path('view_all',views.view_all,name ="view_all"),
    path('view_posts',views.view_posts,name = "view_posts"),
    path('view_reels',views.view_reels, name="view_reels"),
    path('delete_reel',views.delete_reel, name="delete_reel")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)