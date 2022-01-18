from unicodedata import name
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return render( request , 'home.html' )

@csrf_exempt
def show_data(request):
    if request.method == 'POST':
        select = request.POST.get('select')
        print(select)
        if select == 'all_data':
            all_data = UserLevel.objects.values()
            user_data = list(all_data)
            print(user_data)
            return JsonResponse({'status':user_data })

        if select == 'only_django':
            django_data = UserLevel.objects.filter( subject = 'django')
            django_filter = list(django_data.values())
            return JsonResponse({'status':django_filter})

        if select == 'marks_under_45':
            marks_under = UserLevel.objects.filter( marks__lte = 45 )
            
            under = list(marks_under.values())
            return JsonResponse({'status':under})
        if select == 'subject_django_gre_45':
            django_45 = UserLevel.objects.filter(subject = 'django' , marks__lte = 45)
            data = list(django_45.values())
            return JsonResponse({'status':data})
        
        if select == 'without_django':
            without_django = UserLevel.objects.exclude(subject = 'django').values()
            without_d =  list(without_django)
            return JsonResponse({'status':without_d})

        if select == 'Above_45':
            above_45 = UserLevel.objects.filter(marks__gte = 45).values()
            data_marks = list(above_45)
            return JsonResponse({'status':data_marks})