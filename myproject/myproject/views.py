from django.http import HttpResponse  #HttpResponse browser ko response dene mai kam aata hai...
from django.shortcuts import render   # render karane ke liye ye code likh do render ho jayega 
from contact.models import Contact

def aboutUs(request):
    return HttpResponse("<b>YADAV SURAJ</b>") # httpresponse return hota hai koi bhi text dikhana ho to agar text bold karna hai to aap <b> tag ka used kar sakte ho


def homePage(request):
    data = {                     # view file se data kaise bhejte hai html file mai....
        'title':"Home New",
        'clist':['PHP','DJANGO','PYTHON','JAVA']  # how to pass list data from view to html file using for loop....
    }
    return render(request,"index.html",data) # koi html file ko render karana hai kisi bhi link pe aesa karane ka ... render mai 2 parameter leta hai isliye (request) ko liya hai

def contactUs(request):
    return HttpResponse("<b>Contact US</b>")

def userForm(request):
    finalans=0
    if request.method=="POST":
        # n1=int(request.Get['num1']) # ye code ki vajh se aap form ka data get kara sakte ho
        # n2=int(request.Get['num2'])
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))    # two values ko addition kara sakte ho 
         finalans = n1 + n2
    return render(request,"userform.html",{'output':finalans})

def calculator(request):
    result=''
    if request.method=="POST":
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=="+":
            result = n1 + n2
        elif opr=="-":
            result = n1 - n2
        elif opr=="*":
            result = n1 * n2
        elif opr=="/":
            result = n1 / n2
    return render(request,"calculator.html",{'result':result})


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        en=Contact(name=name,email=email)
        en.save()
        return render(request, 'success.html')

    return render(request, 'contact_form.html')