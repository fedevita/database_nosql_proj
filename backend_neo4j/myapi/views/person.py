from django.http import JsonResponse
from myapi.models import Person
from django.views.decorators.csrf import csrf_exempt
import json
from neomodel import db

def getAllPersons(request):
    if request.method == 'GET':
        try:
            persons = Person.nodes.all()
            response = []
            for person in persons :
                obj = {
                  "uid": person.uid,
                  "id": person.id,
                  "first_name": person.first_name,
                  "last_name": person.last_name,
                  "email": person.email,
                  "gender": person.gender,
                  "address": person.address,
                  "phone": person.phone,
                  "country": person.country,
                  "country_code": person.country_code,
                  "bank_id": person.bank_id,
                  "is_pep": person.is_pep,
                  "password": person.password,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

def writePersons(request):
    response=[]
    with open('/home/federico/db2-project/expdata.json', 'r') as f:
        i=0
        my_json_obj = json.load(f)
        response={"ok": ":)"}
        try:
          with db.transaction:
              for person in my_json_obj :
                people = Person.create(person)
              #people = Person.create({"id":"00096ecb-a6e6-4265-9b65-fa9af11a1bfa","first_name":"Cammy","last_name":"Wauchope","email":"cwauchopell@usda.gov","gender":"Genderqueer","address":"040 Algoma Circle","phone":"327 419 9945","country":"France","country_code":"FR","bank_id":"","is_pep":"0","password":"24fc1047d32d89ecc7e0a3f798668f33c59b202bedfb6dfcde7a50928a81964b"})
        except Exception as e:
            response = {"error": "Error occurred in  " + str(e)}
            return JsonResponse(response, safe=False)
        return JsonResponse(response, safe=False)

def deletePersons(request):
    if request.method == 'GET':
        try:
            persons = Person.nodes.all()
            response = []
            for person in persons :
                person.delete()
            response = {"success": "Persons deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)






#@csrf_exempt
#def personDetails(request):
#    if request.method == 'GET':
#        # get one person by name
#        name = request.GET.get('name', ' ')
#        try:
#            person = Person.nodes.get(name=name)
#            response = {
#                "uid": person.uid,
#                "name": person.name,
#                "age": person.age,
#            }
#            return JsonResponse(response, safe=False)
#        except :
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)
#
#    if request.method == 'POST':
#        # create one person
#        json_data = json.loads(request.body)
#        name = json_data['name']
#        age = int(json_data['age'])
#        try:
#            person = Person(name=name, age=age)
#            person.save()
#            response = {
#                "uid": person.uid,
#            }
#            return JsonResponse(response)
#        except :
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)
#
#    if request.method == 'PUT':
#        # update one person
#        json_data = json.loads(request.body)
#        name = json_data['name']
#        age = int(json_data['age'])
#        uid = json_data['uid']
#        try:
#            person = Person.nodes.get(uid=uid)
#            person.name = name
#            person.age = age
#            person.save()
#            response = {
#                "uid": person.uid,
#                "name": person.name,
#                "age": person.age,
#            }
#            return JsonResponse(response, safe=False)
#        except:
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)
#
#    if request.method == 'DELETE':
#        # delete one person
#        json_data = json.loads(request.body)
#        uid = json_data['uid']
#        try:
#            person = Person.nodes.get(uid=uid)
#            person.delete()
#            response = {"success": "Person deleted"}
#            return JsonResponse(response, safe=False)
#        except:
#            response = {"error": "Error occurred"}
#            return JsonResponse(response, safe=False)