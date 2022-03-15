from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.template import Template
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from my_app import forms,serializer
from rest_framework import viewsets,permissions,generics
import urllib.request,json

import urllib.parse as urlparse
from urllib.parse import parse_qs

from django.template.loader import select_template , get_template , render_to_string
from my_app import models


class ProductViewSet(viewsets.ModelViewSet):

    #queryset = models.products.objects.all()
    serializer_class = serializer.products_serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = models.products.objects.all()
       
        arr = self.request.query_params
        for x in arr:
 
            filter = x
            search_string = arr[x]
            queryset =  queryset.filter(**{ filter: search_string })
          
           
       
       
       
        return queryset
    
    

    

# Create your side views here.
def check_if_rating_exists(req,rating_col , slug ):

    
    for index,x in enumerate(rating_col):
    
        if(x['slug'] == slug):
            if(req.method == 'GET'):
                return x['rating']
            else:
                rating_col[index]["rating"] = req.POST.get("rating")
                return 1
         
    return 0



# Create your main views here.

def home(request):
    return render(request,"nav.html")
    


#User Code
@login_required
def logouter(req):
    logout(req)
    return redirect("/products=all")

def logginner(req):
    if req.method == "POST" :
        
        username = req.POST.get("username")
        password = req.POST.get("password")
        print(username , "    " ,password)
        user = authenticate(req,username = username , password = password)

        if user:
            if user.is_active:
                login(req,user)
                return redirect("/products=all")
        else :
         
            return render(req,"accounts.html" , {'msg' : "Incorrect Username Or Password" } )

def accounts(req):

    if(req.method == "POST"):
        target_form = forms.accounter(data=req.POST)

        if target_form.is_valid():
        
            user = target_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            models.acounter.objects.get_or_create(user = user , user_rating = [])
            username = req.POST.get("username")
            password = req.POST.get("password")
            print(username , "    " ,password)
            user = authenticate(req,username = username , password = password)

            if user:
                if user.is_active:
                    login(req,user)
                    return redirect("/products=all")


    return render(req,"accounts.html" , {'register_form'  : forms.accounter  } )

def authenticationer(req):
    if(req.user.is_authenticated and req.user and req.user.is_active):
        return True

def user_rating(req):
    if(req.method == 'POST'):

        rating_col = models.acounter.objects.filter(user = req.user).values('user_rating')[0]['user_rating']

      
  
        if( check_if_rating_exists(req , rating_col , req.POST.get("slug")) == 0 ):
            rating_col.append({ 'slug' : req.POST.get("slug") , 'rating' : req.POST.get("rating") })
            
         
        models.acounter.objects.filter(user = req.user).update(user_rating = rating_col)

    return HttpResponse("Success")


#Store Code
def store(req):
    return render(req , "store.html" , { 'data' : models.products.objects.filter(special = True) })

def details(req,slug):
    rating = {'rating' : False}
    index = 0
    if(authenticationer(req) ):
        if models.acounter.objects.filter(user=req.user ):
            rating_col = models.acounter.objects.filter(user = req.user).values('user_rating')[0]['user_rating']
            checker = check_if_rating_exists(req,rating_col,slug)
           
            rating["rating"] = checker
      
        else:
            print("no rating here")
    return render(req , "details.html" , {"product" : models.products.objects.filter(slug = slug).get() , "rating" : rating })

def products(req,typer="all"):
    
    reponse = urllib.request.urlopen("http://127.0.0.1:8000/api/products_api/")
    
   
    if(req.is_ajax()):


        if(req.GET.get("target") == "true"):
            reponse = urllib.request.urlopen("http://127.0.0.1:8000/api/products_api/?typpe=" +req.GET.get("type") )
        else:
    
            reponse = urllib.request.urlopen("http://127.0.0.1:8000/api/products_api/")

        jsoner = json.load(reponse)
        return render(req,"products-temp.html",{ 'data' : jsoner["results"]  })
       
       

       
    jsoner = json.load(reponse)
    #return temp.render(context={ 'data' : models.products.objects.all() , 'counter' : [1,2,3,4,5]}, request=req)
    return render(req , "products.html" , { 'data' :  jsoner["results"] , 'type' : typer })