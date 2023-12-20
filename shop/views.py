
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blog.models import Post

def Products(request):
    latest1 = Post.objects.filter(category='NEWS').order_by('-timestamp')[:1]
    latest = Post.objects.filter(category='NEWS').order_by('-timestamp')[0:3]
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
    return render(request,'shop.html',context)
