from platform import java_ver
from django.http import JsonResponse

# this is use for third party imports

from rest_framework.response import Response
from rest_framework.views import APIView


# class view

class TestVIew(APIView):

    def  get(self, request, *args , **kwargs):
        data ={        
        'name' : 'dhurv',
        'age' : 23
        }
        return Response(data)


# Create your views here.

# def home(request):
#     data ={
        
#         'name' : 'dhurv',
#         'age' : 23
#     }
#     return JsonResponse(data)
