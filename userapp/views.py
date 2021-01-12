from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from userapp.models import Student
from userapp.serializer import StudentModelSerializer



class StudentGenerAPIView(generics.RetrieveUpdateDestroyAPIView,
                          generics.CreateAPIView,
                          generics.ListCreateAPIView,
                          ):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(self, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class StudentViewSet(ViewSet):
    def stu_login(self, request, *args, **kwargs):
        return Response("成功")
