from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'api/home.html')
def about(request):
    return render(request, 'api/about.html')
