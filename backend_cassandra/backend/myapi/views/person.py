from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapi.models import Person
from myapi.serializers import PersonSerializer
from cassandra.query import (PreparedStatement, BoundStatement, SimpleStatement,
                             BatchStatement, BatchType, dict_factory, TraceUnavailable)
from cassandra.cluster import Cluster


def getPerson(request,username):
    cluster = Cluster(protocol_version = 3)
    session = cluster.connect()
    if request.method == 'GET':
        try:
            results = session.execute("SELECT * FROM db2_100.person WHERE username = %s", (username, ))
            person = results.one()
            serializer = PersonSerializer(person )
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            response = {"error": "Error occurred in  " + str(e)}
            return JsonResponse(response, safe=False)

def createTablePerson(request):
    cluster = Cluster(protocol_version = 3)
    session = cluster.connect()
    if request.method == 'GET':
        try:
            session.execute("DROP TABLE IF EXISTS db2_100.person")
            session.execute("CREATE TABLE db2_100.person (  id VARCHAR ,first_name VARCHAR ,last_name VARCHAR ,email VARCHAR ,gender  VARCHAR ,address VARCHAR ,phone VARCHAR ,country  VARCHAR ,country_code VARCHAR ,bank_id VARCHAR ,is_pep TINYINT  ,password VARCHAR ,PRIMARY KEY (id))")
            response = {"ok": "table person refreshed"}
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred in  " + str(e)}
            return JsonResponse(response, safe=False)




def writePersons(request):
    cluster = Cluster(protocol_version = 3)
    session = cluster.connect()
    with open('/home/federico/db2-project/dataset/cassandra/person.json', 'r') as f:
        my_json_obj = json.load(f)
        batch = BatchStatement(BatchType.LOGGED)
        response = {"ok": ":)"}
        i=0
        for persona in my_json_obj:
          i=i+1
          batch.add("INSERT INTO db2_100.person(id,first_name,last_name,email,gender,address,phone,country,country_code,bank_id,is_pep,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (persona["id"],persona["first_name"],persona["last_name"],persona["email"],persona["gender"],persona["address"],persona["phone"],persona["country"],persona["country_code"],persona["bank_id"],persona["is_pep"],persona["password"]))
          if i%100==0:
              try:
                session.execute_async(batch).result()
                batch = BatchStatement(BatchType.LOGGED)
              except Exception as e:
                  response = {"error": "Error occurred in  " + str(e)}
                  return JsonResponse(response, safe=False)
        return JsonResponse(response["ok"]+str(i), safe=False)




