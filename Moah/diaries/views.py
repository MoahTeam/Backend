from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.core.paginator import Paginator, PageNotAnInteger
# from diaries.forms import FormFromSomeModel as DetailForm
from django.http import Http404, HttpResponse

from .models import Diary, DiaryImage

@login_required
def diary_post_view(request, id=None):
    if request.method == 'GET':
        if id is not None:
            diary = Diary.objects.get(id = id)
            print(diary)
            return render(request, 'Diary/Diary-Writing.html', {'diary' : diary})
        return render(request, 'Diary/Diary-Writing.html', {'diary' : 'False'})
    else:
        if id is None:
            diary = Diary.objects.create(
                writer = request.user,
                title = request.POST.get('title'),
                secure = request.POST.get('secure'),
                content = request.POST.get('content')
            )
            # if request.FILES.get('image'):
            #     DiaryImage.objects.create(
            #         diary = diary,
            #         image = request.FILES.get('image')
            #     )
        else:
            diary = Diary.objects.get(id = id)
            title = request.POST.get('title')
            secure = request.POST.get('secure')
            content = request.POST.get('content')
            
            diary.content = content
            diary.title = title
            diary.secure = secure
            diary.save()
        return redirect('diaries:diary-list')

@login_required
def diary_post_image(request, id=None):
    if id is not None:
        file = request.FILES['image']
        diary = Diary.objects.get(id = id)
        try:
            DiaryImage.objects.get(image = file, writer = request.user)
        except DiaryImage.DoesNotExist:
            DiaryImage.objects.create(
                writer = request.user,
                image = file,
                created_at = diary.created_at,
            )
        print("수정")
    else:
        file = request.FILES['image']
        DiaryImage.objects.create(
            writer = request.user,
            image = file,
        )
        print("생성")
    return HttpResponse('success')

@login_required
def diary_delete_image(request, id):
    file = request.POST.get('file')
    diary = Diary.objects.get(id = id)
    print("@@@@@@@", file)
    
    return HttpResponse('success')

@login_required  
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