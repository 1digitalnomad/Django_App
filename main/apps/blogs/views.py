from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'blogs/index.html')

def new(request):
    response = 'Placeholder to display a new form to create a new blog'
    return HttpResponse(response)


def create_blog(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['blog_name'])
        print(request.POST['blog_desc'])
        print("*"*50)
        return redirect("/blogs")
    else:
        return redirect("/blogs")

def show(request, number):
    response = 'Placeholder to display blog '
    return HttpResponse(response + number)

def edit(request, number):
    response = 'placeholder to edit blog '
    return HttpResponse(response + number)

def destroy(request, number):
    return redirect('/')

