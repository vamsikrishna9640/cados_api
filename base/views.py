from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from  .models import Advocate , Company
from .serializers import AdvocateSerializer, CompanySerializer

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = [ '/advaocates', 'advacate/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocate_list(request):

    if request.method == 'GET':
        #/advocates/?query=vamsi

        query = request.GET.get('query')

        if query == None:
         query =''

        advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response (serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many = False)

        return Response(serializer.data)
    


# class based view
class AdvocateDetails(APIView):
    def get_object(self, username):
      try:
         return Advocate.objects.get(username=username)
      except Advocate.DoesNotExist:
         raise Response('advocate doesnot exists!')
      
   
    def get(self, request, username):
       advocate = self.get_object(username)
       serializer = AdvocateSerializer(advocate, many = False)
       return Response(serializer.data)
    
    def put(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)
    
    def delete(self, request, username):
       advocate = self.get_object(username)
       advocate.delete()
       return Response('user was deleted')
       
       
# @api_view(['GET', 'PUT', 'DELETE'])
# def advoacte_details(request, username):
#     advocate = Advocate.objects.get(username=username)
#     serializer = AdvocateSerializer(advocate, many = False)

#     if request.method == 'GET':
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user was deleted')


class Companies(APIView):
   def get(self, request):
      companies = Company.objects.all()
      serializer = CompanySerializer(companies, many = True)
      return Response(serializer.data)


   