from django.shortcuts import render, redirect
from cout.models import Contact
from django.contrib import messages


def index(request):
 return render(request,'index.html')

def home(request):
    if request.method == 'POST':
        x=request.POST['text']
        y=len(x)
        q=x.split()
        z = len(x.split())
        print(y)
        print(z)
        n=len(x.splitlines())
        print(len(x.splitlines()))

        if y == 1:
         res=render(request,'index.html',{"abc":y,"character":"Character :","ac": z,"words": "Word :","word":"Word Count Report","status":"Status : Successfully counted!"})
         return res
        elif z == 1:
            return render(request,'index.html',{"abc":y,"character":"Characters :","words": "Word :","ac": z,"word":"Word Count Report","status":"Status : Successfully counted!","and":"and"})
        else:
            if n != 1:
             res = render(request, 'index.html', {"abc":(y-2*n)+2,"character":"Characters :","ac": z, "words": "Words :","word":"Word Count Report","status":"Status : Successfully counted!","and":"and"})
             return res
            elif n==1:
             res = render(request, 'index.html',{"abc":y, "character": "Characters :", "ac": z, "words": "Words :","word": "Word Count Report", "status": "Status : Successfully counted!", "and": "and"})
             return res
            else:
                 redirect("/")
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        contact=Contact(name=name,email=email,comment=comment)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')






