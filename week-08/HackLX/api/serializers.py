from rest_framework import serializers
from website.models import Offer, Category



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['title', 'description', 'category', 'author', 'choices', 'id']

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for k,v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    # Smell - Duplicating code
    def update(self, instance, validated_data):
        for k,v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance
