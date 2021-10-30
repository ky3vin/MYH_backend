from rest_framework import serializers
from .models import Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class PhotoSerializer(serializers.ModelSerializer):
    #post내에서 category가 Foreginekey이므로 id로 나타나게 되므로 아래와 같이 추가
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Photo
        fields ='__all__'