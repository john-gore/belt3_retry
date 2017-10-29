from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from django.contrib import messages
def index(request):
    return render(request, "login.html")
def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Logged in!!")
    return redirect("/success")

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    
    return redirect('/dash')
def dash(request):
    this_user = User.objects.get(id = request.session['user_id']) 
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'aliases': User.objects.exclude(id = request.session['user_id']),
        'friends': User.objects.exclude(id = request.session['user_id']),
    }
    return render(request, 'dashboard.html', context)
def profile(request, id):
    this_user = User.objects.get(id = id)
    context = {
       'profile': this_user
    }
    return render(request, 'profile.html', context)
def addedfriend(request, id):
    this_friend = User.objects.get(id = id)
    this_user = User.objects.get(id = request.session['user_id'])
    print this_friend
    print this_user
    return redirect('/dash')
def removedfriend(request, id):
    this_friend = User.objects.get(id = id)
    this_user = User.objects.get(id = request.session['user_id'])
    print this_friend
    print this_user
    return redirect('/dash')