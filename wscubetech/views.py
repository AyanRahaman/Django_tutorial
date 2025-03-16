from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm

def home(request):
    return render(request,"index.html")

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    # return HttpResponse("Welcome to Wscubetech")
    return render(request,"about.html",{"output":output})

def academics(request):
    return render(request,"academics.html")

def admissions(request):
    return render(request,"admissions.html")   

def contact(request):
    return render(request,"contact.html") 
    
def userform(request):
    finalans = 0
    data={}
    # try:
    #     if request.method=="GET":
    #     # n1 = int(request.GET["num1"])
    #     # n2 = int(request.GET["num2"])
    #         n1 = int(request.GET.get("num1"))
    #         n2 = int(request.GET.get("num2"))
    #         # print(n1+n2)
    #         finalans = n1+n2
    # except:
    #     pass  
    
    try:
        if request.method=="POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans,
            }
            
            url="/about/?output={}".format(finalans)
            return redirect(url)
            # return HttpResponseRedirect(url) #-- for redirect into the about page
            
    except:
        pass
    return render(request,"userform.html",data) 


def submitform(request):
    try:
        if request.method == "POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans = n1 + n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': finalans
            }
            
            return HttpResponse(finalans)
            
    except:
        pass


def main(request):
    data = {
        'title': 'Welcome to Django Tutorial',
        'heading':'Welcome to wscubetech | Jodhpur',
        'clist':["php","django","java"],
        'numbers': [10,20,30,40,50,60,70,80,90],
        'student_details': [
            {'name': "Shahidur Rahaman","phone":70299979185},
            {'name': "Wscubetech",'phone':9702997945}
        ]
    }
    return render(request,"main.html",data)

def userForm(request):
    finalans=0
    fn=usersForm()
    
    data={'form':fn}
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request,POST.get("num2"))
            finalans=n1+n2
            data={
                'form':fn,
                'output':finalans
            }
            
    except:
        pass      
            
    

def courses(request):
    return HttpResponse("This is our course page")

# FOR CREATING DYNAMIC --->
def courseDetails(request,course_id):
    return HttpResponse(course_id)




