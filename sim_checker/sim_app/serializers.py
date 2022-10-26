from rest_framework import serializers
from sim_app.models import PhoneNumber



class SimAppSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'phone_number',
            'sim_network'
        )
        model=PhoneNumber