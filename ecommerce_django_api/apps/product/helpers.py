from rest_framework import serializers


class NestedObjCreationMixin:

    def create_nested_object(self, serializer_class, validated_data):
        serializer = serializer_class(data=validated_data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()


class NestedObjectSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        serializer = self.nested_serializer(instance)
        return serializer.data
