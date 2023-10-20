from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from amazon.models import Products


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Products.objects.all())])
    img = serializers.ImageField(required=True)
    description = serializers.CharField(max_length=500, required=True)
    instock = serializers.IntegerField()
    price = serializers.FloatField()


    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
            instance.name = validated_data.get('name')
            instance.img = validated_data.get('img')
            instance.description = validated_data.get('description')
            instance.instock = validated_data.get('instock')
            instance.price = validated_data.get('price')
            instance.save()
            return  instance