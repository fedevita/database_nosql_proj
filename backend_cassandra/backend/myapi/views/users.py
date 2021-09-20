from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapi.models import User
from myapi.serializers import UserSerializer

from cassandra.cluster import Cluster

def getUser(request,username):
    cluster = Cluster(protocol_version = 3)
    session = cluster.connect()
    if request.method == 'GET':
        try:
            session.execute("UPDATE user_management.user_credentials SET password='pipponicchio' WHERE username = %s", (username, ))
            results = session.execute("SELECT * FROM user_management.user_credentials WHERE username = %s", (username, ))
            user = results.one()
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

