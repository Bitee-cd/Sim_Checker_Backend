from rest_framework import serializers
from sim_app.models import PhoneNumber,SimNetwork





class SimSerializer(serializers.ModelSerializer):
    class Meta:
        model=SimNetwork
        fields = ('id','name')

class SimAppSerializer(serializers.ModelSerializer):
    sim=SimSerializer(many=False)
    class Meta:
        model=PhoneNumber
        fields = ('id','phone_number','sim',)

