from rest_framework import serializers
from apps.product.models import *

class ProductSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'