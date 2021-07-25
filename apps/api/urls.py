from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    path('addtional_products', views.show_list, name="additional_products")

]

