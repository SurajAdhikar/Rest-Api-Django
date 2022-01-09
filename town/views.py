

from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import serializers
from .serializer import HelloSerializer, UserPofileSerializer
from town import models

from town import serializer


class HelloApiView(APIView):
    """Test API View"""
    serializers_class = HelloSerializer

    def get(self, request, format= None):
        """Return a list of APIView features"""
        an_apiview = [ 
            'uses HTTP methods as function (get, post, put, patch, delete)',
            'Is  similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello!','an_apiview':'an_apiview'})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            meesage = f'Hello{name}'
            return Response ({'message': 'message'})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request ,pk=None):
        """Handle updating an object """
        return Response({'method':'Put'})

    def patch(self,request , pk=None):
        """Handle a partial update of an object"""
        return Response ({'method':'Patch'})

    def delete(self,request, pk=None):
        """Delete an object"""
        return Response({'method':'Delete'})



class HelloViewSet(viewsets.ViewSet):
    """test API viewSet"""
    serializer_class = HelloSerializer

    def list(self,request):
        """Request a hello message"""

        a_viewset = [
            'Uses actions(list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using routers',
            'Provides functionally in less code',

        ]

        return Response({'message':'hello!','a_viewset':'a_viewset'})


    def create(self,request):
        """Create a hello message"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello{name}!'
            return response ({'message': message})

        else:
            return response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request, pk = None):
        """Handle getting an object by its ID"""
        return Response ({'http_method':'GET'})

    def update(self,request, pk = None):
        """Handle updating an object """
        return response ({'http_method':'PUT'})

    def partial_update(self,request, pk = None):
        """Handle updating part of an object """
        return response ({'http_method':'PATCH'})  

    def destroy(self,request, pk = None):
        """Handle deleting an object """
        return response ({'http_method':'DELETE'}) 

class UserProfileViewSet (viewsets.ModelViewSet):
    """Handle creeating and updating profile"""
    serializer_class= UserPofileSerializer
    queryset = models.UserProfile.objects.all()
