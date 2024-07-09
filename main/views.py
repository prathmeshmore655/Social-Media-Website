import http
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from Social_Media_new import settings
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model



def home(request):

    if request.method == 'POST':

        return render(request,'home.html')
    
    else:


        return redirect('Userlogin')


def Userlogin(request):

    if request.method == 'POST':

        uname = request.POST.get('username')
        pword = request.POST.get('password')

        

        try: 
             user = User.objects.get(username = uname)
             
             
             if check_password(pword,user.password):
                
                

                return account_display(request,user)
             
             else:

                message = "Incorrect Password or Username" 
                return render(request,'home.html',{"message":message})


        except User.DoesNotExist:

            message = "User Does Not EXists"

            return render(request,'home.html',{'message':message})

    else:

        return render(request,'home.html',{})



                

def create_user(request):

    if request.method =='POST':

        return render(request,'user_creation.html')

    else:

        return redirect('Userlogin')




def user(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name').lower()
        l_name = request.POST.get('l_name').lower()
        uname = request.POST.get('email').lower()
        pword = request.POST.get('pword').lower()
        c_pword = request.POST.get('c_pword').lower()

        if pword == c_pword:
            user = User.objects.create_user(username=uname, password=pword) # type: ignore
            user.first_name = f_name
            user.last_name = l_name
            user.save()

            return home(request)
        else:
            message = {
                'text': 'Password and Confirm Password does not match'
            }
            return render(request, 'user_creation.html', {'message' : message})
    else:
        return render(request, 'user_creation.html', {})
    



def profile_sub(request):

    if request.method == "POST":

        user_no = request.POST.get('id_of_user')

        user = User.objects.get(pk = user_no)

        return display_profile(request,user)
    

    else:

        return redirect('Userlogin')



def display_profile(request, user_list):


    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_list.id)

        profile = UserProfile.objects.get(user_id=user.id) # type: ignore

        count = Post.objects.filter(post_no_id=profile.id).count() # type: ignore

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id=user.id).order_by('-created_time')

        user_all = User.objects.all()

        user_except = User.objects.exclude(pk=user_list.id)

        follower_object = Followers.objects.filter(follower_of_id=user_list.id)
        following_object = Followers.objects.filter(follower_name = user_list.username)
        post_exclude = Post.objects.exclude(post_no_id=user_list.id)

        return render(request,'profile.html',{"following":following_object,"follower":follower_object,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })


    else :

        return redirect('Userlogin')





def update_profile(request):


    if request.method == 'POST':        
        user_id = request.POST.get('profile_id')
        profile = UserProfile.objects.get(user_id = user_id)
        user = User.objects.get(pk = user_id)

  

    
        username = request.POST.get('username')
        bio = request.POST.get('bio')
        profile_photo = request.FILES.get('profile_photo')  

       
        user.username = username


        if bio :

            profile.bio = bio
        
        
        if profile_photo:
            profile.profile_picture = profile_photo


        user.save()
        profile.save()

       
        return display_profile(request,user)
    
    else:

        return redirect('Userlogin')



def save_post(request):


    if request.method != 'POST':
        return redirect('Userlogin')

    user_id = request.POST.get('u_id')

    if not user_id:
        return HttpResponseBadRequest("User ID not provided")

    
    
    user = User.objects.get(pk = user_id)
   
    post = Post(post_no=user)

    
    post_file = request.FILES.get('post_file')

    print(post_file)
    if post_file:
        post.post_file = post_file

    post.caption = request.POST.get('caption', '')

    
    post.save()



    return display_profile(request,user)



def delete_post(request):
        

    if request.method == 'POST':    

        user_id = request.POST.get('user')

       

        user = User.objects.get(pk = user_id)
        post_id = request.POST.get('post_id')

       
        try:
            post = Post.objects.get( pk = post_id )
            post.delete()

        except Post.DoesNotExist :

            pass

        return display_profile(request,user)

    else:
            
            return redirect('Userlogin')

   




def social_media(request):

    if request.method == 'POST':

        user_no = request.POST.get('id_of_user')      

        user = User.objects.get(pk = user_no)

        return account_display(request,user)


    else:

        return redirect('Userlogin')






def account_display(request,user_list):
        
    if request.method == 'POST':    

        user = get_object_or_404(User, pk=user_list.id)
        profile = UserProfile.objects.get(user_id=user.id)
        count = Post.objects.filter(post_no_id = profile.id).count()

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id = user.id).order_by('-created_time')


        user_all = User.objects.all()


        user_except = User.objects.exclude(pk = user_list.id)

        post_exclude = Post.objects.exclude(post_no_id = user_list.id)


    

        return render(request,'home_page.html',{"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })

    else:

        
        return redirect('Userlogin')





def visit_profile(request):



    if request.method == 'POST':
        
        user_id = request.POST.get('user_id')

        user = User.objects.get(pk = user_id)

        return display_profile(request,user)
    
    else:

        return redirect('Userlogin')




def post_comments(request):

    if request.method == 'POST':
        user = request.POST.get('user')
        user_list = User.objects.get(pk = user)
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')

        object_of_comment = Comments.objects.create(comments = comment , post_id_id = post_id,comment_By = user_list.id,by_commented = user_list.username)

        object_of_comment.save()


        return account_display(request,user_list)
    
    else:

        return redirect('Userlogin')




def follow(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')  # login_user
        follow_id = request.POST.get('follow_id')  # user which has to be followed
        
        user = get_object_or_404(User, pk=user_id)
        profile_to_follow = get_object_or_404(UserProfile, user_id=follow_id)
        user_profile_to_follow = get_object_or_404(User, pk=follow_id)

        
        follower_exists = Followers.objects.filter(follower_of_id=profile_to_follow.id, follower_name=user.username,follower_of_username = user_profile_to_follow.username).exists()
        
        if follower_exists:
            print("User is already following")

            return account_display(request, user)
        
        follower = Followers(follower_name=user.username, follower_of_id=profile_to_follow.id,follower_of_username = user_profile_to_follow.username)
        follower.save()

        follower_count = Followers.objects.filter(follower_of_id=profile_to_follow.id).count()
        profile_to_follow.followers = follower_count
        profile_to_follow.save()

        following_count = Followers.objects.filter(follower_name=user.username).count()
        profile_who_follow = get_object_or_404(UserProfile, user_id=user_id)
        profile_who_follow.following = following_count
        profile_who_follow.save()

        print("Follow successful")

        return account_display(request, user)

    return redirect('Userlogin')









def unfollow(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        follow_id = request.POST.get('follow_id')
        
        user = get_object_or_404(User, pk=user_id)
        profile_to_unfollow = get_object_or_404(UserProfile, user_id=follow_id)
        
        follower = Followers.objects.filter(follower_of_id=profile_to_unfollow.id, follower_name=user.username).first()
        
        if follower:
            follower.delete()
            
            follower_count = Followers.objects.filter(follower_of_id=profile_to_unfollow.id).count()
            profile_to_unfollow.followers = follower_count
            profile_to_unfollow.save()
            
            following_count = Followers.objects.filter(follower_name=user.username).count()
            user_profile = get_object_or_404(UserProfile, user_id=user_id)
            user_profile.following = following_count
            user_profile.save()

            return account_display(request, user)
        
        return account_display(request, user)

    return redirect('Userlogin')





def visit_profile(request):

    if request.method == "POST":

        user_id = request.POST.get('user_id')
        login_user = request.POST.get('login_user_id')
        user_list = User.objects.get(pk = user_id)


        return vistor_display_profile(request,user_list,login_user)

    else :

        
        return redirect('Userlogin')

        



def vistor_display_profile(request,user_list,login_user_list):
        

    if request.method == "POST":

    
        user = get_object_or_404(User, pk=user_list.id)
        profile = UserProfile.objects.get(user_id=user.id)
        count = Post.objects.filter(post_no_id = profile.id).count()

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id = user.id).order_by('-created_time')


        user_all = User.objects.all()

        user_except = User.objects.exclude(pk = user_list.id)


        login_user_list = User.objects.get(pk = login_user_list)


        login_user_exclude = User.objects.exclude(pk = login_user_list.id)


        post_login_exclude = Post.objects.exclude(pk = user_list.id)

        post_exclude = Post.objects.exclude(post_no_id = user_list.id)




        
        return render(request,'visited_profile.html',{"post_login_exclude":post_login_exclude,"login_user_exclude":login_user_exclude,"login_user":login_user_list,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })

    else:

        return redirect('Userlogin')







def view_comments(request):


    if request.method == 'POST':

        post_id = request.POST.get('receive_post_id')

        user_id = request.POST.get('user_id')


        user_list = User.objects.get(pk = user_id)

        return view_comment_account_display(request,user_list,post_id)

    else:

        return redirect('Userlogin')








def view_comment_account_display(request,user_list,post_id):


    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_list.id)
        profile = UserProfile.objects.get(user_id=user.id)
        count = Post.objects.filter(post_no_id = profile.id).count()

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id = user.id).order_by('-created_time')


        user_all = User.objects.all()


        user_except = User.objects.exclude(pk = user_list.id)

        post_exclude = Post.objects.exclude(post_no_id = user_list.id)


        comment_posts = Comments.objects.filter(post_id_id = post_id)




        return render(request,'home_page.html',{"comment_posts":comment_posts,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })


    else:

        return redirect('Userlogin')





def like(request):

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        post_id = request.POST.get('post_id')
        user_list = get_object_or_404(User, pk=user_id)
        post = get_object_or_404(Post, pk=post_id)

        if post.likes.filter(id=user_id).exists():

            return account_display(request, user_list)
        else:

            post.likes.add(user_list)

            post.no_of_likes = post.likes.count()

            post.save()


        return account_display(request, user_list)
    
    else:

        return redirect('Userlogin')







def get_comments(request, post_id):
    try:
        comments = Comments.objects.filter(post_id=post_id).values('comment_By', 'by_commented', 'comments')
        comments_list = list(comments)
        return JsonResponse({'comments': comments_list})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




def visit_javascript__profile(request,user_id):

    user = User.objects.get(pk = user_id)

    return display_profile(request,user)






def search_page(request):


    if request.method == 'POST':

        id_of_user = request.POST.get('id_of_user')

        login_user = User.objects.get(pk = id_of_user)




        return render(request,'search.html',{"login_user":login_user})

    else:

        return redirect('Userlogin')



def reels_page(request):

    if request.method == 'POST':    

        id_of_user = request.POST.get('id_of_user')

        login_user = User.objects.get(pk = id_of_user)

        reels = Reels.objects.exclude(reels_no_id = login_user.id)

        return render(request,'reels.html',{"login_user":login_user,"reels":reels})

    else:

        return redirect('Userlogin')





def search_action(request):

    if request.method == 'POST':    


        user_id = request.POST.get('user_id')

        search_query = request.POST.get('search_query')


        if not search_query:

            return search_page_render(request, user_id, "Please enter a search query.")

        try:

            users = User.objects.filter(username__icontains=search_query).exclude(pk = user_id)

        except Exception as e:

            users = f"An error occurred: {str(e)}"

        if users.exists():
            return search_page_render(request, user_id, users)
        else:
            return search_page_render(request, user_id, "User Profile Does Not Exist")


    else:

        return redirect('Userlogin')



def search_page_render(request, user_id, users):

    if request.method == 'POST':    

        try:
            login_user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return render(request, 'search.html', {"error": "Logged-in user not found."})

        return render(request, 'search.html', {"login_user": login_user, "search_results": users})

    else:

        return redirect('Userlogin')





def upload_reel(request):


    if request.method == 'POST':
        video = request.FILES.get('video')
        caption = request.POST.get('caption')
        user_id = request.POST.get('user_id')

        reels = Reels.objects.create(reel_video = video , caption = caption , reels_no_id = user_id)


        reels.save()  

        login_user = User.objects.get(pk = user_id)
        reels = Reels.objects.exclude(reels_no_id = login_user.id)



    
        return render(request,'reels.html',{"login_user":login_user,"reels":reels})
    


    else:

        return redirect('Userlogin')
    


def view_posts(request):


    if request.method == 'POST':


        user_id = request.POST.get('user_id')

        user_list = User.objects.get(pk = user_id)

        user = get_object_or_404(User, pk=user_list.id)

        profile = UserProfile.objects.get(user_id=user.id) 

        count = Post.objects.filter(post_no_id=profile.id).count() 

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id=user.id).order_by('-created_time')

        user_all = User.objects.all()

        user_except = User.objects.exclude(pk=user_list.id)

        follower_object = Followers.objects.filter(follower_of_id=user_list.id)
        following_object = Followers.objects.filter(follower_name = user_list.username)
        post_exclude = Post.objects.exclude(post_no_id=user_list.id)

        return render(request,'profile.html',{"following":following_object,"follower":follower_object,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })


    else :

        return redirect('Userlogin')






def view_all(request):


    if request.method == 'POST':


        user_id = request.POST.get('user_id')

        user_list = User.objects.get(pk = user_id)

        user = get_object_or_404(User, pk=user_list.id)

        profile = UserProfile.objects.get(user_id=user.id) 

        count = Post.objects.filter(post_no_id=profile.id).count() 

        post = Post.objects.all()

        post_of_user = Post.objects.filter(post_no_id=user.id).order_by('-created_time')

        reels_of_user =Reels.objects.filter(reels_no_id = user.id).order_by

        user_all = User.objects.all()

        user_except = User.objects.exclude(pk=user_list.id)

        follower_object = Followers.objects.filter(follower_of_id=user_list.id)
        following_object = Followers.objects.filter(follower_name = user_list.username)
        post_exclude = Post.objects.exclude(post_no_id=user_list.id)

        return render(request,'profile.html',{"reels_of_user":reels_of_user,"following":following_object,"follower":follower_object,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"post_of_user": post_of_user,"user_except":user_except })


    else :

        return redirect('Userlogin')















def view_reels(request):


    if request.method == 'POST':


        user_id = request.POST.get('user_id')

        user_list = User.objects.get(pk = user_id)

        user = get_object_or_404(User, pk=user_list.id)

        profile = UserProfile.objects.get(user_id=user.id) 

        count = Post.objects.filter(post_no_id=profile.id).count() 

        post = Post.objects.all()

        reels_of_user = Reels.objects.filter(reels_no_id=user.id).order_by('-uploaded_time')

        user_all = User.objects.all()

        user_except = User.objects.exclude(pk=user_list.id)

        follower_object = Followers.objects.filter(follower_of_id=user_list.id)
        following_object = Followers.objects.filter(follower_name = user_list.username)
        post_exclude = Post.objects.exclude(post_no_id=user_list.id)

        return render(request,'profile.html',{"reels_of_user":reels_of_user,"following":following_object,"follower":follower_object,"post_exclude":post_exclude,"user":user,"profile":profile,"post":post,"count":count,"user_all":user_all,"user_except":user_except })


    else :

        return redirect('Userlogin')








def delete_reel(request):
        

    if request.method == 'POST':    

        user_id = request.POST.get('user')

       

        user = User.objects.get(pk = user_id)
        post_id = request.POST.get('post_id')

       
        try:
            post = Reels.objects.get( pk = post_id )
            post.delete()

        except Reels.DoesNotExist :

            pass

        return display_profile(request,user)

    else:
            
            return redirect('Userlogin')

   