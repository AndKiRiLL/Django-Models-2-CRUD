from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Form, FormEdit
from App.models import User

def index(request):

        lenght = User.objects.count()

        list = []
        for i in range(0, lenght):

            user_current = User.objects.get(pk=i+1)
            list.append({'email': user_current.email, 'password': user_current.password, 'login': user_current.login})


        return render(request, 'index.html', context={'list': list})



def form_edit(request):

    if request.method == "POST":

        index = request.POST.get('index', 1)

        user = User.objects.get(pk=index)

        user.email    = request.POST.get('email', 'Undefined')
        user.password = request.POST.get('password', 'Undefined')
        user.login    = request.POST.get('login', 'Undefined')

        user.save()
        return HttpResponseRedirect('/')

    else:
        form_edit = FormEdit()
        return render(request, 'form.html', context={'form_edit': form_edit})


def form_add(request):

    if request.method == "POST":

        email    = request.POST.get('email', 'Undefined')
        password = request.POST.get('password', 'Undefined')
        login    = request.POST.get('login', 'Undefined')

        User.objects.create(email = email, password = password, login = login)
        return HttpResponseRedirect('/')

    else:
        form = Form()
        return render(request, 'form_add.html', context={'form': form})
