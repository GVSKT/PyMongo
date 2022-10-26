from rest_framework import serializers
from todoPymongo.models import demo

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = demo
        fields = ('userid', 'username', 'task', 'status', 'status_time', 'updation_time')
        #fields = '__all__'



