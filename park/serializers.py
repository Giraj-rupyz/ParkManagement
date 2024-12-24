from rest_framework import serializers
from .models import UserTypeDiscount, Ticket


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserTypeDiscount
        fields='__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['name', 'age', 'user_type', 'price']