from django.shortcuts import render

from .models import Post

def index(request):
    post_list = Post.objects.all()
    context ={
        'post_list': post_list
    }
    return render(request, 'main.html', context)

# Create your views here.
def post_list_view(request):
    #post_list = Post.objects.all()
    post_list = Post.objects.filter(writer = request.user)
    context = {
        'post_list': post_list
    }
    return render(request, 'posts/moahtodo.html', context)