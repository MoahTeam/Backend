from django.shortcuts import get_object_or_404, render, redirect

from todo.forms import TodoBaseForm, TodoForm

from .models import Todo

from django.contrib.auth.decorators import login_required

def index(request):
    todo_list = Todo.objects.all()
    context ={
        'todo_list': todo_list
    }
    return render(request, 'main.html', context)

# Create your views here.
def todo_list_view(request):
    #todo_list = Todo.objects.all()
    todo_list = Todo.objects.filter(writer = request.user)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todo/moahtodo.html', context)

def moahtodo(request):
    return render(request, 'todo/moahtodo.html')

# 글 작성 html
def todo_new_view(request) :
    return render(request, 'todo/moahtodonew.html')

# # 글 저장 함수
def todo_create_view(request) :
    if(request.method == "POST"):
        post = Todo() # post 변수에 Todo 객체 생성

        post.todolist = request.POST['todolist']

        post.save() # model 객체. save()를 통해 모델 객체를 DB에 저장
    return redirect('todo')



def djangocreate(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        # 유효한 데이터 타입이라면
        if form.is_valid():
            post = Todo()
            post.checkbox = form.cleaned_data['checkbox']
            post.todolist = form.cleaned_data['todolist']
            post.save() # model 객체
            return redirect ('todo')
        
    else:
        form = TodoForm()
    return render(request, 'form_create.html', {'form':form})



@login_required
# def todo_create_view(request):
#     if request.method == 'GET':
#         return render(request, 'todo/moahtodo.html', {'form': TodoBaseForm()})
#     else:
#         #image = request.FILES.get('image')
#         content = request.POST.get('content')
#         Todo.objects.create(
#             #image = image,
#             content = content,
#             #writer = request.user
#         )
        #return redirect('todo/moahtodo.html')

# def todo_save_view(request):
#     if request.method == 'POST':
#         form = TodoBaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo:todo-save')  # 저장 후 redirect할 URL (todo-save는 해당 페이지의 이름)
#     else:
#         form = TodoBaseForm()
#     return render(request, 'todo/moahtodo.html', {'form': form})

def todo_save_view(request):
    if request.method == 'POST':
        form = TodoBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo-save') # 저장 후 redirect할 URL (todo-save는 해당 페이지의 이름)
    else:
        form = TodoBaseForm()
    return render(request, 'todo/moahtodo.html', {'form': form})

