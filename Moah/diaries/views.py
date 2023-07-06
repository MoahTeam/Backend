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
        Diary.objects.create(
            image = request.FILES.get('image'),
            content = request.POST.get('content'),
            writer = request.user,
            feeling = request.POST.get('feeling'),
            title = request.POST.get('title'),
            secure = request.POST.get('secure'),
        )
        return redirect('diary-list')
    
def diary_list_view(request, id):
    print("@@@@@",id)
    if id == None:
        id = DateFormat(datetime.now()).format('m')
    if request.method == 'GET':
        Diary.objects.filter(created_at__month=id)
        try:
            post_list = Diary.objects.filter(writer = request.user)
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

    return render(request, 'Diary/Diary.html', {'post_list': post_list, 'page_obj':page_obj, 'paginator':paginator})