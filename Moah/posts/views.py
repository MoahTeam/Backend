from django.shortcuts import get_object_or_404, render, redirect

from posts.forms import PostBaseForm

from .models import Post

from django.contrib.auth.decorators import login_required

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

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/moahtodo.html', {'form': PostBaseForm()})
    else:
        #image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(
            #image = image,
            content = content,
            #writer = request.user
        )
        #return redirect('posts/moahtodo.html')