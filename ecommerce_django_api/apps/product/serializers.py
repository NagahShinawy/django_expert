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
            return self.validate_uuid(data)
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




