from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..first_app.models import User
from django.contrib import messages
def index(request):
    return render(request, "profile.html")
