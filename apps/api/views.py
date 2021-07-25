from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSeriallizer
from apps.product.models import Show
# Create your views here.

@api_view(['GET'])
def overView(request):
    api_urls = {
        'List':'/list',
    }
    return Response(api_urls)

@api_view(['POST'])
def show_list(request):
    # 자료 가져오기
    serializer = ProductSeriallizer(data=request.data)

    
    shows = Show.objects.all()
    serializer = ProductSeriallizer(shows, many=True)
    return Response(serializer.data)