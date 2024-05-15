from rest_framework import serializers
from .models import GuestBook

class guestBookSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = GuestBook
        fields = "__all__"

    def check_object_permissions(self, request, obj):
        if request.data['password'] != obj.password:
            raise serializers.ValidationError("wrong password error")
        return