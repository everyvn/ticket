from django.urls import path
from .views import *
app_name = "core"

urlpatterns = [
    # 메인페이지용
    path('', main_page, name='main_page'),

]

