from rest_framework  import serializers
from .models import mail

class mail_serializer (serializers.ModelSerializer):
    class Meta:
        model=mail
        fields = '__all__'


