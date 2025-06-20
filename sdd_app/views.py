from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
 
class SampleAPIView(APIView):
    def get(self, request):
        data = {
            "message": "Hello, from ..... ",
            "status": "success",
            "data": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"},
                {"id": 3, "name": "Item 3"},
            ]
        }
        return Response(data)