from django.shortcuts import render
from .models import Post
def index (request):
    post=Post.objects.create(
        title="Title",
        content="This is a content" , 
    )
    return render(request,'index.html')

