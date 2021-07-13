from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Show
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.


