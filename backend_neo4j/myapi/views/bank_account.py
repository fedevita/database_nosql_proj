from django.http import JsonResponse
from myapi.models import Bank_account
from django.views.decorators.csrf import csrf_exempt
import json
from neomodel import db
from py2neo import Graph
from py2neo.bulk import create_nodes


def writeBankAccounts(request):
    response=[]
    with open('/home/federico/db2-project/dataset/bank_account.json', 'r') as f:
        g = Graph("bolt://localhost:7687", auth=("neo4j", "db2"))
        my_json_obj = json.load(f)
        response={"ok": ":)"}
        try:
          create_nodes(g.auto(), my_json_obj, labels={"Bank_account"})
          #with db.transaction:     
          #    #for person in my_json_obj :
          #    #  people = Person.create(person)
          #    #people = Person.create({"id":"00096ecb-a6e6-4265-9b65-fa9af11a1bfa","first_name":"Cammy","last_name":"Wauchope","email":"cwauchopell@usda.gov","gender":"Genderqueer","address":"040 Algoma Circle","phone":"327 419 9945","country":"France","country_code":"FR","bank_id":"","is_pep":"0","password":"24fc1047d32d89ecc7e0a3f798668f33c59b202bedfb6dfcde7a50928a81964b"})
        except Exception as e:
            response = {"error": "Error occurred in  " + str(e)}
            return JsonResponse(response, safe=False)
        return JsonResponse(response, safe=False)

def deleteBankAccounts(request):
    if request.method == 'GET':
        
        try:
            #persons = Person.nodes.all()
            #response = []
            #for person in persons :
            #    person.delete()
            graph = Graph("bolt://localhost:7687", auth=("neo4j", "db2"))
            graph.run("MATCH (n:Bank_account) DETACH  DELETE n")
            response = {"success": "Persons deleted"}
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred in  " + str(e)}
            return JsonResponse(response, safe=False)
