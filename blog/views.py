
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import Link 
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateLink

@login_required
def urlform(request):

    if request.method == "POST":
        
        urlforme=CreateLink(request.POST)
        if urlforme.is_valid():
            obj = urlforme.save(commit=False)
            obj.user = request.user
            obj.save()
            
            urlforme.save()
            messages.success(request, f'Успешно добавлено!')
            return redirect('url')
    else:
        urlforme = CreateLink()
    news = Link.objects.filter(user=request.user)
    news=Link.objects.all()
    data = {
         'urlforme': urlforme,
         'title':'Добавление ссылки',
         'news': news
     }      
    return render(request, 'blog/url.html', data)
        

    
    
def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контакты!'})
def glav(request):
    return render(request, 'blog/glav.html', {'title': 'Страница контакты!'})
