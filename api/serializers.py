from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone_number',
            'is_varified',
            'invaiting_code',
            'refferal_code'
        )
