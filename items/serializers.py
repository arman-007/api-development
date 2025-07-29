from decimal import Decimal
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty")
        if len(value) > 100:
            raise serializers.ValidationError("Name must be 100 characters or less.")
        return value
    
    def validate_price(self, value):
        if not isinstance(value, Decimal):
            try:
                value = Decimal(str(value))
            except (ValueError, TypeError):
                raise serializers.ValidationError("Price must be a valid decimal number")
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_description(self, value):
        if value and len(value) > 1000:
            raise serializers.ValidationError("Description must be 1000 characters or less.")
        return value
    
class ItemCreateSerializer(ItemSerializer):
    def validate(self, attrs):
        """Cross-field validation"""
        # You can add cross-field validation here if needed
        return attrs

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'price': {'required': False},
        }

    def validate_name(self, value):
        if value is not None:
            if not value or not value.strip():
                raise serializers.ValidationError("Name cannot be empty")
            return value.strip()
        return value

    def validate_price(self, value):
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Price must be greater than 0")
            if value > 999999999:
                raise serializers.ValidationError("Price cannot exceed $9,999,999.99")
        return value

    def validate_description(self, value):
        if value is not None:
            return value.strip()
        return value