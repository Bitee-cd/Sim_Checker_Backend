from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from sim_app.models import PhoneNumber
from sim_app.models import SimNetwork
from sim_app.serializers import SimAppSerializer
from sim_app.serializers import SimSerializer
from rest_framework import status
from rest_framework.decorators import api_view
 
 

@api_view(['GET'])
def getRoutes(request):
    routes ={
        "list of all phone numbers":"{baseUrl}/phone_number/",
        "list of all sim":"{baseUrl}/phone_number/sim",
        "detail of sim":"{baseUrl}/phone_number/{id}",
        "find details of sim":"{baseUrl}/phone_number/find/{number}"

    }
    return Response(routes)



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
        print(serializer.data)
        if (len(serializer.data)>0):
            data=serializer.data
            message="Success",
            return Response({"data":data,"message":message,}, status=status.HTTP_200_OK)
        else:
            data=[]
            message="Sorry, data not found in database"
            return Response({"message":message}, status=status.HTTP_404_NOT_FOUND)
       

