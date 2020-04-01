from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delate)',
            'IS similiar to a tradition django view',
            'Gives you the most control of your application logic',
            'IS mapped manueally to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
