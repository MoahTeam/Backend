from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.core.paginator import Paginator, PageNotAnInteger

from .models import Diary

@login_required
def diary_post_view(request):
    if request.method == 'GET':
        return render(request, 'Diary/Diary-Writing.html')
    else:
        print("@@@@@@@@@",request.POST.get('secure'))
        Diary.objects.create(
            image = request.FILES.get('image'),
            content = request.POST.get('content'),
            writer = request.user,
            
            title = request.POST.get('title'),
            secure = request.POST.get('secure'),
        )
        return redirect('diaries:diary-list')
    
def diary_list_view(request, id=None):
    print("@@@@@",id)
    if id == None:
        id = DateFormat(datetime.now()).format('m')
    if request.method == 'GET':
        try:
            post_list = Diary.objects.filter(writer = request.user, created_at__month=id)
        except:
            post_list = ""
        
        page = request.GET.get('page')
        paginator = Paginator(post_list, 9)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.num_pages
            print("SDSFDFDf", page)
            page_obj = paginator.page(page)

    return render(request, 'Diary/' + str(id).lstrip("0") + '.html', {'post_list': post_list, 'page_obj':page_obj, 'paginator':paginator})