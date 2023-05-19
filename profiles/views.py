from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles import serializers
from profiles import models
from profiles import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is Similar to a traditional django View',
            'Gives you the most control over application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
             )


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request,pk=None):
        """Delete an object"""
        return Response({"method":"DELETE"})



class HelloViewSet(viewsets.ViewSet):
    """Test API VIEWSETS"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "uses action (list, create, update, partialupdate)",
            "automatically maps to urls using routers",
            "provides more functionality with less code"
        ]

        return Response({"message":"Hello!", 'a_viewset': a_viewset})


    def create(self, request):
        """Create Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request,pk=None):
        """Handle getting an object by its id."""
        return Response({"http_method": "GET"})


    def update(self, request,pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})


    def partial_update(self, request,pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})


    def destroy(self, request,pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
