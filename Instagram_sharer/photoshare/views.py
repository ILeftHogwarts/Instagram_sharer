from django.shortcuts import render, Http404, HttpResponse, redirect
from django.template import RequestContext, loader
from .models import User, InstaPost, PostTags
import sys, requests, json
from .forms import TagForm

params = {
    "client_id": "2c08b7e83d75448a99765ae283c5b0f5",
    "client_secret": "1d7aa18351394069a476839b1505df6a",
    "redirect_uri": "http://ilefthogwarts.pythonanywhere.com",
    "access_token": '5922489674.2c08b7e.5ea1bdda33b34df3b64898639249c6e9',
    "count": 20
    }

def posts_recive(request):
    r = requests.get("https://api.instagram.com/v1/users/self/",params=params)
    data = json.loads(r.text)
    user_id = data['data']['id']
    access_token = params['access_token']
    post_r = requests.get("https://api.instagram.com/v1/users/{0}/media/recent/".format(user_id),params=params)
    posts_data = json.loads(post_r.text)
    try:
        current_user = User.objects.get(user_id = user_id)
    except User.DoesNotExist as ex:
        current_user = User(name = data['data']['full_name'],user_id = user_id,access_token = access_token)
        current_user.save()
    for post in posts_data['data']:
        if 'videos' in post:
            type = 'videos'
        else:
            type = 'images'
        try:
            InstaPost.objects.get(user_post = current_user, url = post[type]['standard_resolution']['url'], type = type)    
        except InstaPost.DoesNotExist as ex:
            inst_post = InstaPost(user_post = current_user, url = post[type]['standard_resolution']['url'], type = type)
            inst_post.save()
            for tag in post['tags']:
                try:
                    curr_tag = PostTags.objects.get(tag = tag)
                except PostTags.DoesNotExist:
                    curr_tag = PostTags(tag = tag)
                    curr_tag.save()
                inst_post.tag.add(curr_tag)
            inst_post.save()
    return redirect("main_page")

def main_page(request):
    if request.method == "GET":
        filter_form = TagForm(request.GET)
        tag = request.GET.get("select_tag")
        try:
            current_user = User.objects.get(name = "Andrew Diemientiev")
            if tag == None or tag == " ":
                posts = InstaPost.objects.filter(user_post = current_user)
            else:
                taged_post = PostTags.objects.get(tag = tag)
                posts = InstaPost.objects.filter(user_post = current_user, tag = taged_post)  
        except User.DoesNotExist as ex404:
            raise Http404('User does not exist')
    else:
        filter_form = TagForm(initial = [" "])
        try:
            current_user = User.objects.get(name = "Andrew Diemientiev")
            posts = InstaPost.objects.filter(user_post = current_user)
        except User.DoesNotExist as ex404:
            raise Http404('User does not exist')
    return render(request, "photoshare/main_page.html", {'posts': posts,'form': filter_form})
    
        

    
    

