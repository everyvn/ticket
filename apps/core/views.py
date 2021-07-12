from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.


def main_page(request, category_slug=None):
    current_category = None
    if category_slug:
        current_category = ""
    context ={'current_category':current_category}
    return render(request, 'core/core.html', context)