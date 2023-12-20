from django.urls import path
from . import views



app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail,name='post_detail'),
    #path('post/<slug>/', views.post, name = 'post'),
   # path('about/', views.about,name = 'about' ),
    #path('postlist/<slug>/', views.postlist, name = 'postlist'),
   # path('posts/', views.allposts, name = 'allposts'),
]
