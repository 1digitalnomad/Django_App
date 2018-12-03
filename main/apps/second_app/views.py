from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')

def create(request):
    print('*'*50)
    print(request.POST)
    print(request.POST['second_app_name'])
    print(request.POST['second_app_desc'])
    print('*'*50)
    return redirect('/second_app')

