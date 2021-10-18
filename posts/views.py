from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from guardian.shortcuts import get_objects_for_user
from django.contrib.contenttypes.models import ContentType

from .models import SimpleModel
from .serializer import SimpleModelSerializer,Simple_User_based_permission_ModelSerializer
from .permission import ReadOnly


class SimpleModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    serializer_class = SimpleModelSerializer
    queryset = SimpleModel.objects.all()


class ListPosts(APIView):

    permission_classes = [IsAuthenticated ]
    def get(self, request, format=None):
        # queryset = SimpleModel.objects.all()
        queryset = get_objects_for_user(request.user, 'posts.view_project')
        serializer_class=Simple_User_based_permission_ModelSerializer(queryset,context={'request': request},many=True)
        return Response({"message": serializer_class.data , "status": 200})


class ListPosts2(APIView):

    permission_classes = [IsAuthenticated ]
    def get(self, request, format=None):
        queryset = get_objects_for_user(request.user, 'posts.view_simplemodel')
        serializer_class=Simple_User_based_permission_ModelSerializer(queryset,context={'request': request},many=True)
        return Response({"message": serializer_class.data , "status": 200})