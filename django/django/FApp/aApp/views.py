from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    msg = """<h1>hello vasanth</h2> <br/>
    Name
    <input type='text' placeholder='name'/>
    Password
    <input type='password' placeholder='password'/>
    
    """
    return HttpResponse (msg)

def wish(request):
    msg = '<h1 style=color:red;>hello vasanth welcome</h2>'
 
    return HttpResponse (msg)    
