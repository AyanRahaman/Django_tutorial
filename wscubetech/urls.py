"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wscubetech import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('main/',views.main),
    path('about/',views.about,name="about"),
    path('academics/',views.academics,name="academics"),
    path('admissions/',views.admissions,name="admissions"),
    path('contact/',views.contact,name="contact"),
    path('courses/',views.courses),
    # ========== FOR SLUG ==========
    # path('courses/<int:course_id>',views.courseDetails), ----- for int
    # path('courses/<str:course_id>',views.courseDetails), ----- for str
    # path('courses/<slug:course_id>',views.courseDetails) ----- for slug
    path('courses/<course_id>',views.courseDetails) # this is use if the type is not mentioned, thats menas you dont jnow whether it is int,str or slug
        
]
