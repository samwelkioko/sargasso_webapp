
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post



def post_list(request):
    latest1 = Post.objects.filter(category='NEWS').order_by('-timestamp')[:1]
    latest = Post.objects.filter(category='NEWS').order_by('-timestamp')[1:]
    events = Post.objects.all().filter(category='EVENT').order_by('-timestamp')[0:3]
    posts = Post.objects.all().filter(category='NEWS')[1:]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 8)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    
    context= {
     
        'posts': posts,
        'latest':latest,
        'latest1':latest1,
        'page_obj': page_obj,
        'events': events,
        

       
    }
    return render(request,'home/index.html',context)


def post_detail(request,slug):

    post = get_object_or_404(Post, slug=slug)
    latest = Post.objects.filter(category='NEWS').order_by('-timestamp')[0:3]
    events = Post.objects.all().filter(category='EVENT').order_by('-timestamp')[0:3]
    context = {
        'post': post,
        'latest':latest,
        'events': events,
    }
    return render(request,'single.html',context )

