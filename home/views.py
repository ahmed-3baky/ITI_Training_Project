from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def home(request) : 
    my = {
        "name" : "ahmed abd elbaki " ,
        "age" : 21 , 
        "tl" : "Full stack web developer" , 
        "exp" : 5
    }
    
    return render(request , "home.html" , context={"my": my} )

def about(request)  :
    
    about_ =  { 
               "name" : "The Information Technology Institute (ITI)",
               "tl" : "established back in 1993 and became one of the MCITs affiliates in 2005" , 
               "exp" : 19
               
        } 
    return render(request,"about.html" , context={"me": about_})

def contact(request)  : 
    return render (request,"contact.html")