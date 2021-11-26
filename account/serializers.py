from rest_framework import serializers

from account.models import MyUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.Charfield(min_length=6, write_only=True)
    password_confirm = serializers.Charfield(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        
