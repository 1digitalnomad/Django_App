from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # print(request.__dict__)
    return render(request, 'first_app/index.html')


def create(request):
    if request.method == "POST":
        print(request.__dict__)
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        print("*"*50)
        return redirect("/first_app")
    else:
        return redirect("/first_app")
