from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateformat import DateFormat

from .models import Diary

@login_required
def diary_post_view(request):
    if request.method == 'GET':
        return render(request, 'Diary/Diary.html')
    else:
        Diary.objects.create(
            image = request.FILES.get('image'),
            content = request.POST.get('content'),
            writer = request.user,
            feeling = request.POST.get('feeling'),
            title = request.POST.get('title'),
            secure = request.POST.get('secure'),
        )
        return redirect('diary_list')
    
def diary_list_view(request):
    if request.method == 'GET':
        #Diary.objects.filter(created_at__month=3)
        #today = DateFormat(datetime.now()).format('m') => 07
        post_list = Diary.objects.filter(writer = request.user)
        context = {
            'post_list':post_list
        }
    return render(request, 'Diary/.html', context)