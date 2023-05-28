import uuid
from rest_framework import serializers
from .models import Brand, Category


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
        if not isinstance(value, (Brand, Category)):
            return None
        return True
