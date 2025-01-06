from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import dish
from .serializers import chiefSerializer
from rest_framework import status,parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = dish.objects.all()
    serializer_class = chiefSerializer
    

    def get_serializer_class(self):
        if self.action == 'list':
            return chiefSerializer
        if self.action == 'create':
            return chiefSerializer
        return self.serializer_class
    
   
    #get all books

    def list(self,request):
        try:
            chief_objs = dish.objects.all()
            serializer = self.get_serializer(chief_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add book
    def create(self,request):
        try:
            serializer =self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage': dish added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single book
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #chief_objs = dish.objects.all()
                chief_objs = self.get_object()
                serializer = self.get_serializer(chief_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of book
    def update(self,request, pk=None):
        try:
            #chief_objs = dish.objects.all()
            chief_objs = self.get_object()
            serializer = self.get_serializer(chief_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage': dish updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields

    def partial_update(self,request, pk=None):
        try:
            #chief_objs = dish.objects.all()
            chief_objs = self.get_object()
            serializer = self.get_serializer(chief_objs,data=request.data,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage': dish updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request,pk):
        try:
            id=pk
            book_obj = self.get_object()
            book_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage': dish deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })