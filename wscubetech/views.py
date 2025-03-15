from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request):
    # return HttpResponse("Welcome to Wscubetech")
    return render(request,"about.html")

def academics(request):
    return render(request,"academics.html")

def admissions(request):
    return render(request,"admissions.html")   

def contact(request):
    return render(request,"contact.html") 
    
def userform(request):
    finalans = 0
    try:
        # n1 = int(request.GET["num1"])
        # n2 = int(request.GET["num2"])
        n1 = int(request.GET.get("num1"))
        n2 = int(request.GET.get("num2"))
        # print(n1+n2)
        finalans = n1+n2
    except:
        pass    
    return render(request,"userform.html",{'output':finalans}) 


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



def courses(request):
    return HttpResponse("This is our course page")

# FOR CREATING DYNAMIC --->
def courseDetails(request,course_id):
    return HttpResponse(course_id)




