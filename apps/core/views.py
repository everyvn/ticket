from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from apps.product.models import *
# Create your views here.


def main_page(request, category_slug=None):
    current_category = None
    shows = Show.objects.all()
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
    context ={
        'current_category':current_category,
        'shows': shows
        }
    return render(request, 'core/core.html', context)