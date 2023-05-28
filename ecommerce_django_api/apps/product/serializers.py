from rest_framework import serializers
from .models import Brand, Product, Category
from .fields import NestedObjectField
import uuid


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


# class ProductSerializer(serializers.ModelSerializer):
#     brand = BrandSerializer()
#     category = CategorySerializer()
#
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#     def create(self, validated_data):
#         brand_data = validated_data.pop("brand")
#         category_data = validated_data.pop("category")
#         brand = NestedObjCreationMixin().create_nested_object(BrandSerializer, brand_data)
#         category_data = NestedObjCreationMixin().create_nested_object(CategorySerializer, category_data)
#         return Product.objects.create(**validated_data, brand=brand, category=category_data)


class BrandField(NestedObjectField):

    def to_representation(self, value):
        if super().to_representation(value) is None:
            return None
        return BrandSerializer(value).data


class CategoryField(NestedObjectField):

    def to_representation(self, value):
        if super().to_representation(value) is None:
            return None
        return CategorySerializer(value).data


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandField()
    category = CategoryField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        brand_data = validated_data.pop('brand', None)
        category_data = validated_data.pop('category', None)
        brand = self.create_nested_object(BrandSerializer, brand_data)
        category = self.create_nested_object(CategorySerializer, category_data)
        return Product.objects.create(brand=brand, category=category, **validated_data)

    def create_nested_object(self, serializer_class, data):
        if isinstance(data, dict):
            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            return serializer.save()
        elif isinstance(data, uuid.UUID):
            try:
                return serializer_class.Meta.model.objects.get(pk=data)
            except serializer_class.Meta.model.DoesNotExist:
                raise serializers.ValidationError(f"Invalid {serializer_class.Meta.model.__name__} data")
        else:
            raise serializers.ValidationError(f"Invalid {serializer_class.Meta.model.__name__} data")




