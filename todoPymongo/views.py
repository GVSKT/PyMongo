from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action,api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
import datetime
from datetime import datetime
from rest_framework import status
from .models import demo
from .serializers import  UserSerializer
from .db_config import pymongo_db

class Creation_Class(APIView):
    def get(self,request, format=None):
        try:
            user_data = JSONParser().parse(request)
            myquery = ({"username":user_data['username']})
            mycol = pymongo_db()
            users = mycol.find(myquery)
            user_serializer = UserSerializer(users, many=True)
            return Response(user_serializer.data)

        except Exception as ex:
            return Response({"Exception Occurred For GET Method Request": str(ex)})

    def post(self,request, format=None):

        try:
            user_data = JSONParser().parse(request)
            mycol = pymongo_db()
            user_serializer = UserSerializer(data=user_data)

           if user_serializer.is_valid():
                user_serializer.save()
                return Response("Insertion Successful")
            return Response("Insertion Failed")

        except Exception as ex:
            return Response( {"Exception Occurred For Insertion Request" : str(ex) })



class Manipulation_Class(APIView):
    @csrf_exempt
    def put(self,request,id):
        try:
            mycol = pymongo_db()
            user_data = JSONParser().parse(request)
            print("\nuser_data : ", user_data)
            user_data['updation_time'] = datetime.now()
            myquery = {"userid": id }
            newvalues = {"$set": user_data}
            mycol.update_one(myquery, newvalues)
            return Response("Updated Successfully")

        except Exception as ex:
            return Response( {"Exception Occurred For Updation Request" : str(ex) })


    def delete(self,request,id):
        try:
            mycol = pymongo_db()
            user_data = JSONParser().parse(request)
            mycol.delete_one({"userid":id})
            return Response({"Status": "Deletion Successful"}, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({"Exception Occurred For Deletion Request" : str(ex)})

