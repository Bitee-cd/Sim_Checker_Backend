from rest_framework import generics

from sim_app.models import PhoneNumber
from sim_app.serializers import SimAppSerializer

class ListSimApp(generics.ListCreateAPIView):
    queryset=PhoneNumber.objects.all()
    serializer_class=SimAppSerializer

class DetailSimApp(generics.RetrieveUpdateDestroyAPIView):
    queryset=PhoneNumber.objects.all()
    serializer_class=SimAppSerializer