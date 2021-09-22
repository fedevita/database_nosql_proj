#from django.http import JsonResponse
#from myapi.models import User
#from django.views.decorators.csrf import csrf_exempt
#import json
#from neo4j import GraphDatabase
#import sys

#def getUser(request,username):
#    if request.method == 'GET':
#        try:
#            user = User.nodes.get(username = username)
#            response = {
#                "uid":   user.uid,
#                "username": user.username,
#                "password": user.password,
#            }
#            return JsonResponse(response, safe=False)
#        except :
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)
#
#def writeUser(request):
#    response=[]
#    with open('/home/federico/db2-project/neo4j_dataset/USERS_DATA.json', 'r') as f:
#        i=0
#        my_json_obj = json.load(f)
#        response=[]
#        for el in my_json_obj :
#            i=i+1
#            try:
#                username = el['username']
#                password = el['password']
#                user = User(username=username, password=password)
#                user.save()
#                response.append({"id": user.id})
#            except :
#                
#                response = {"error": "Error occurred in  " + str(i)}
#                return JsonResponse(response, safe=False)
#        return JsonResponse(response, safe=False)
#
#def getAllUsers(request):
#    if request.method == 'GET':
#        try:
#            user = User.nodes.all()
#            response = []
#            for user in user :
#                obj = {
#                "id":   user.id,
#                "username": user.username,
#                "password": user.password,
#                }
#                response.append(obj)
#            return JsonResponse(response, safe=False)
#        except:
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)
#
#def deleteAllUsers(request):
#    if request.method == 'GET':
#        uri = "neo4j://localhost:7687"
#        driver = GraphDatabase.driver(uri, auth=("neo4j", "db2"))
#        try:
#            with driver.session() as session:
#                session.write_transaction(delete_all_users)
#            response = {"ok":"all good"}
#            return JsonResponse(response, safe=False)
#        except:
#            response = {"error": "Error occurred"+str(sys.exc_info()[0])}
#            return JsonResponse(response, safe=False)
#
#def delete_all_users(tx):
#        tx.run("MATCH (n: User) DELETE n ")
#