from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is Similar to a traditional django View',
            'Gives you the most control over application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

        
