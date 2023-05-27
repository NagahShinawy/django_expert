from rest_framework import serializers
from .models import Brand, Product, Category
from .helpers import NestedObjCreationMixin, NestedObjectSerializer
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


class NestedObjectField(serializers.Field):
    def validate_uuid(self, uuid_):
        try:
            return uuid.UUID(uuid_)
        except ValueError:
            raise serializers.ValidationError("Invalid UUID format")

    def to_internal_value(self, data):
        if isinstance(data, dict):
            return data
        elif isinstance(data, str):
            self.validate_uuid(data)
        else:
            raise serializers.ValidationError("Invalid data format")

    def to_representation(self, value):
        if isinstance(value, Brand):
            return BrandSerializer(value).data
        if isinstance(value, Category):
            return CategorySerializer(value).data
        return None


class ProductSerializer(serializers.ModelSerializer):
    brand = NestedObjectField()
    category = NestedObjectField()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        brand_data = validated_data.pop('brand', None)
        category_data = validated_data.pop('category', None)

        brand = None
        category = None

        if brand_data is not None:
            if isinstance(brand_data, dict):
                brand_serializer = BrandSerializer(data=brand_data)
                brand_serializer.is_valid(raise_exception=True)
                brand = brand_serializer.save()
            elif isinstance(brand_data, uuid.UUID):
                try:
                    brand = Brand.objects.get(pk=brand_data)
                except Brand.DoesNotExist:
                    raise serializers.ValidationError("Invalid brand data")
            else:
                raise serializers.ValidationError("Invalid brand data")

        if category_data is not None:
            if isinstance(category_data, dict):
                category_serializer = CategorySerializer(data=category_data)
                category_serializer.is_valid(raise_exception=True)
                category = category_serializer.save()
            elif isinstance(category_data, uuid.UUID):
                try:
                    category = Category.objects.get(pk=category_data)
                except Category.DoesNotExist:
                    raise serializers.ValidationError("Invalid category data")
            else:
                raise serializers.ValidationError("Invalid category data")

        product = Product.objects.create(brand=brand, category=category, **validated_data)

        return product




