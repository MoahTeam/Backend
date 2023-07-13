from audioop import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from datetime import datetime
from django.utils.dateformat import DateFormat

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
    day = DateFormat(datetime.now()).format('d')
    month = DateFormat(datetime.now()).format('m')
    todo_list = Todo.objects.filter(writer = request.user, created_at__month=month, created_at__day = day)
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


# 투두리스트 작성
def djangocreate(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        # 유효한 데이터 타입이라면
        if form.is_valid():
            post = Todo()
            #post.checkbox = form.cleaned_data['checkbox']
            post.todolist = form.cleaned_data['todolist']
            post.save() # model 객체
            #return redirect('moahtodo')    
            return redirect(reverse('moahtodo'))    
    else:
        form = TodoForm()
    return render(request, 'todocreate.html', {'form':form})

def moahtodo(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo/moahtodo.html', {'todo_list' : todo_list})

# 메인화면에 투두리스트 띄우기
def maincreate(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        # 유효한 데이터 타입이라면
        if form.is_valid():
            post = Todo()
            post.checkbox = form.cleaned_data['checkbox']
            post.todolist = form.cleaned_data['todolist']
            post.save() # model 객체
            #return redirect('moahtodo')    
            return redirect(reverse('main'))    
    else:
        form = TodoForm()
    return render(request, 'main.html', {'form':form})

def main(request):
    todo_list = Todo.objects.all()
    return render(request, 'main.html', {'todo_list' : todo_list})


# 투두리스트 삭제1
def delete_button_view(request):
    if request.method == 'POST':
        # POST 요청인 경우에만 처리합니다.
        button_id = request.POST.get('button_id')  # 삭제 버튼의 ID 값을 가져옵니다.
        # 버튼을 클릭한 데이터를 데이터베이스에서 찾습니다.
        if not button_id:
                    # button_id가 비어있으면 예외 처리
                    return redirect('todo:error_page')
        try:
            data = Todo.objects.get(id=button_id)  # 데이터베이스 모델과 필드를 적절히 변경해야 합니다.
        except Todo.DoesNotExist:
            # 해당 데이터가 없으면 적절한 예외 처리를 수행합니다.
            return redirect('todo:error_page')  # 에러 페이지로 리디렉션하거나 다른 처리를 수행합니다.
        # 데이터를 삭제합니다.
        data.delete()
        # 삭제 후 남은 항목들을 조회합니다.
        remaining_items = Todo.objects.all()
        # 삭제 후 리디렉션할 페이지로 이동합니다.
        return render(request, 'todo/success_page.html', {'remaining_items': remaining_items})  # 삭제 후 성공 페이지로 리디렉션하거나 다른 처리를 수행합니다.
    # POST 요청이 아닌 경우에는 해당 페이지를 보여줍니다.
    return render(request, 'todo/moahtodo.html')  # 적절한 템플릿과 경로를 설정해야 합니다.

def error_page(request):
    return render(request, 'todo/error_page.html')

def success_page(request):
    remaining_items = Todo.objects.all()
    return render(request, 'todo/success_page.html', {'remaining_items': remaining_items})

def back_to_moahtodo(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo/moahtodo.html', {'todo_list' : todo_list})

# # 투두리스트 삭제2
# def delete_button2_view(request):
#     if request.method == 'POST':
#         # POST 요청인 경우에만 처리합니다.
#         button_id2 = request.POST.get('button_id2')  # 삭제 버튼의 ID 값을 가져옵니다.
#         # 버튼을 클릭한 데이터를 데이터베이스에서 찾습니다.
#         if not button_id2:
#                     # button_id가 비어있으면 예외 처리
#                     return redirect('todo:error_page')
#         try:
#             data = Todo.objects.get(id=button_id2)  # 데이터베이스 모델과 필드를 적절히 변경해야 합니다.
#         except Todo.DoesNotExist:
#             # 해당 데이터가 없으면 적절한 예외 처리를 수행합니다.
#             return redirect('todo:error_page')  # 에러 페이지로 리디렉션하거나 다른 처리를 수행합니다.
#         # 데이터를 삭제합니다.
#         data.delete()
#         # 삭제 후 남은 항목들을 조회합니다.
#         remaining_items = Todo.objects.all()
#         # 삭제 후 리디렉션할 페이지로 이동합니다.
#         return render(request, 'todo/success_page2.html', {'remaining_items': remaining_items})  # 삭제 후 성공 페이지로 리디렉션하거나 다른 처리를 수행합니다.
#     # POST 요청이 아닌 경우에는 해당 페이지를 보여줍니다.
#     #return render(request, 'todo/moahtodo.html')  # 적절한 템플릿과 경로를 설정해야 합니다.
#     todo_list = Todo.objects.all()
#     return render(request, 'todo/moahtodo.html', {'todo_list' : todo_list})

# # 투두리스트 삭제3
# def delete_button3_view(request):
#     if request.method == 'POST':
#         # POST 요청인 경우에만 처리합니다.
#         button_id = request.POST.get('button_id3')  # 삭제 버튼의 ID 값을 가져옵니다.
#         # 버튼을 클릭한 데이터를 데이터베이스에서 찾습니다.
#         if not button_id:
#                     # button_id가 비어있으면 예외 처리
#                     return redirect('todo:error_page')
#         try:
#             data = Todo.objects.get(id=button_id)  # 데이터베이스 모델과 필드를 적절히 변경해야 합니다.
#         except Todo.DoesNotExist:
#             # 해당 데이터가 없으면 적절한 예외 처리를 수행합니다.
#             return redirect('todo:error_page')  # 에러 페이지로 리디렉션하거나 다른 처리를 수행합니다.
#         # 데이터를 삭제합니다.
#         data.delete()
#         # 삭제 후 남은 항목들을 조회합니다.
#         remaining_items = Todo.objects.all()
#         # 삭제 후 리디렉션할 페이지로 이동합니다.
#         return render(request, 'todo/success_page3.html', {'remaining_items': remaining_items})  # 삭제 후 성공 페이지로 리디렉션하거나 다른 처리를 수행합니다.
#     # POST 요청이 아닌 경우에는 해당 페이지를 보여줍니다.
#     return render(request, 'todo/moahtodo.html')  # 적절한 템플릿과 경로를 설정해야 합니다.




def todo_list_view(request):
    #post_list = Post.objects.all()
    todo_list = Todo.objects.filter(writer = request.user)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todo/todo_list.html', context)



def todo_save_view(request):
    if request.method == 'POST':
        form = TodoBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo-save') # 저장 후 redirect할 URL (todo-save는 해당 페이지의 이름)
    else:
        form = TodoBaseForm()
    return render(request, 'todo/moahtodo.html', {'form': form})

