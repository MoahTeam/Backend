from datetime import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from diaries.models import DiaryImage

@login_required
def gallery_view(request, month=None, day=None):
    if month == None:
        month = DateFormat(datetime.now()).format('m')
    if day == None:
        day = DateFormat(datetime.now()).format('d')
    print("month:",month,"day:",day)
    if request.method == 'GET':
        array = ""
        image_array = []
        for i in range(0,32):
            image_count = DiaryImage.objects.filter(created_at__month=month, created_at__day = i).count()
            array = array + str(image_count)
        print(array)
        try:
            images = DiaryImage.objects.filter(created_at__month=month, created_at__day = day)
        except DiaryImage.DoesNotExist:
            images = []
        for image in images:
            image_array.append(image)
        print("@@@@@@image_array", image_array)
    return render(request, 'gallery/' + str(month).lstrip("0") + '.html', {'image_count': array, 'image_array' : image_array, 'month' : month, 'day': day })

#calendarDay.innerText = "{% if image_count %}영ㅅ{% endif %}";