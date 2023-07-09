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
        return render(request, 'Diary/Diary-Writing.html')
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
            new_image = request.FILES.get('image')
            content = request.POST.get('content')

            if new_image:
                diary.image.delete()
                diary.image = new_image
            
            diary.content = content
            diary.save()
        return redirect('diaries:diary-list')
    
def diary_post_image(request, id=None):
    if id is not None:
        diary = Diary.objects.get(id = id)
        print(DateFormat(diary.created_at).format('m'))
        first_date = datetime.date(DateFormat(diary.created_at).format('Y'), DateFormat(diary.created_at).format('m'), DateFormat(diary.created_at).format('d'))
        images = DiaryImage.objects.get(wirter=request.user, created_at__range=(first_date, first_date))
        images.delete()
    file = request.FILES['image']
    DiaryImage.objects.create(
                writer = request.user,
                image = file,
    )
    print("만듬")
    return HttpResponse('success')
    
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