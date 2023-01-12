from django.shortcuts import get_object_or_404

from .models import  ToDo
from .serializers import ToDoSerializer

from django.contrib.auth.models import User


from rest_framework.views import APIView
# rest-framework api imports
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


# Create your views here.

class ToDoList(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Select user
        user = request.user
        # Search all objects of list by user
        todo = ToDo.objects.filter(user=user)       
        # serializes all object
        serializers = ToDoSerializer(todo, many=True)
        # Show list of object
        return JsonResponse(serializers.data, safe=False, status=status.HTTP_200_OK)
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        
        data = {
            "task" : request.data['task'],
            "description" : request.data['description'],
            "user" : request.user.id
        }
        
        # serializes data entry
        objSerializer = ToDoSerializer(data=data)
        # verify if entry is valid
        if objSerializer.is_valid(): 
            # save entry               
            objSerializer.save()    
            # show object saved 
            return JsonResponse(objSerializer.data, safe=False, status=status.HTTP_201_CREATED)
        # show errors because not save  
        print(objSerializer.errors)
        return JsonResponse(objSerializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    
class ToDoOperations(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        # Select user
        user = request.user
        # Search all objects of list by user
        todo = get_object_or_404(user, id__iexact = id)
        if todo.user == user:
            # serializes all object
            serializers = ToDoSerializer(todo, many=True)
            # Show list of object
            return JsonResponse(serializers.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse("The task you try open is registered of otrher user!", safe=False, status=status.HTTP_401_UNAUTHORIZED)
        
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        # Select user
        user = request.user
        # Search all objects of list by user
        todo = get_object_or_404(ToDo, id__iexact = id)
        if todo.user == user:    
            
            data = {
                "task" : request.data['task'],
                "description" : request.data['description'],
                "user" : request.user.id
            }       
            
            # serializes data entry 
            serializer = ToDoSerializer(todo, data=data)
            # verify if entry is valid
            if(serializer.is_valid()):
                # save entry               
                serializer.save()     
                # show object updated    
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
            # show errors because not save 
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse("The task you try update is registered of otrher user!", safe=False, status=status.HTTP_401_UNAUTHORIZED)
    
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        # Search object by id
        # Select user
        user = request.user
        # Search all objects of list by user
        todo = get_object_or_404(ToDo, id__iexact = id)
        if todo.user == user:    
            # delete entry                 
            todo.delete()    
            # show blank object (deleted)   
            return JsonResponse( f'Task {id} was deleted successful' ,safe=False, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse("The task you try delete is registered of otrher user!", safe=False, status=status.HTTP_401_UNAUTHORIZED)

