from django.shortcuts import render

def home_view(request):
    return(request,'Home_Page/Home.html')
