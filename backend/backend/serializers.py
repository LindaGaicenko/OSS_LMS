from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {'required': False, 'allow_blank': True},
        }

    def validate(self, data):
        data['username'] = data.get('email')
        return super().validate(data)