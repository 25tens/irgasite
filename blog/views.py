from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

#def post_list(request):
#    post_list= Post.objects.all()
#    return render(request,'blog/post_list.html',{'post_list':post_list,})

def index(request):
    post_list= Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list,})