from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from sim_app.models import PhoneNumber
from sim_app.models import SimNetwork
from sim_app.serializers import SimAppSerializer
from sim_app.serializers import SimSerializer

class ListSim(APIView):
    def get(self,request):
        sims = SimNetwork.objects.all()
        serializer=SimSerializer(sims,many=True)
        return Response(serializer.data)

class ListPhoneNumber(generics.ListCreateAPIView):
    queryset=PhoneNumber.objects.all()
    serializer_class=SimAppSerializer

class DetailSimApp(generics.RetrieveUpdateDestroyAPIView):
    queryset=PhoneNumber.objects.all()
    serializer_class=SimAppSerializer

class FindSim(APIView):
    def get(self,request, number_):
        number = PhoneNumber.objects.filter(phone_number=number_)
        serializer = SimAppSerializer(number, many=True)
        return Response(serializer.data)

