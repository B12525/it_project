from django.shortcuts import render
from django.http import HttpRedirect
from .forms import UserForm

def register_name(request):
    if request.method == "post":
        form = UserForm(request.post)
        if form.is_valid:
            return HttpRedirect('/Home_Page/')
    else:
        UserForm()

    return render(request, 'regist.html',{'form' : form })
