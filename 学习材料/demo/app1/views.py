from django.shortcuts import render
from app1 import models

# Create your views here.
def index(request):
    user_list = []
    users = models.MyUser.objects.all()
    for user in users:
        username = user.username
        password = user.password
        user_list.append((username, password))

    context = {
        'user_list': user_list,
    }
    return render(request, 'index.html', context)