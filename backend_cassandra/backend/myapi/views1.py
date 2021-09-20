from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Here is the import for the python driver
from cassandra.cluster import Cluster

class User(APIView):

    def get(self, request, username):
        cluster = Cluster(protocol_version = 3)
        session = cluster.connect()
        results = session.execute("SELECT * FROM user_management.user_credentials WHERE username = %s", (username, ))
        user = results.one()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        pass


