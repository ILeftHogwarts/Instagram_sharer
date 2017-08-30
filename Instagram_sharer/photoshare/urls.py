from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.main_page, name='main_page'),
    url(r'^post_receive/',views.posts_recive, name='post_receive'),
]
