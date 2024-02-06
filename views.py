from django.shortcuts import render
from django.views.generic.base import View
from .models import Post
class PostView(View):
    #вывод записей
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog/blog.html", {"post_list":posts})
class PostDetail(View):
    def get(self, request, pk):
        post = Post.oblects.get(id=pk)
        return render(request,"blog/blog_detail.html",{"post":post})


# Create your views here.
