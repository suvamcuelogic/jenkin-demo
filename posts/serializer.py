from django.contrib.auth.models import User, Group , Permission
from rest_framework import serializers
from .models import SimpleModel
from guardian.shortcuts import assign_perm

class Permission_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ['name',"codename"]


class Group_Serializer(serializers.ModelSerializer):
    allowed_permissions=serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['name',"allowed_permissions"]

    def get_allowed_permissions(self, obj):
        permissions=Permission.objects.filter(group=obj)
        data=Permission_Serializer(permissions,many=True)
        return data.data


class SimpleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleModel
        fields = '__all__'

    def create(self, validated_data):
        post =SimpleModel.objects.create(**validated_data)
        # assign_perm('assign_post', self.context['request'].user, post)
        # assign_perm('view_project', self.context['request'].user, post)
        assign_perm('change_simplemodel',post.author, post)
        assign_perm('delete_simplemodel', post.author, post)
        return post


class Simple_User_based_permission_ModelSerializer(serializers.ModelSerializer):
    permission_crud = serializers.SerializerMethodField()
    object_level_permission = serializers.SerializerMethodField()
    permission_level = serializers.SerializerMethodField()

    class Meta:
        model = SimpleModel
        fields = ["author","title","description","status","datetime","permission_crud","object_level_permission","permission_level"]

    def get_permission_crud(self,obj):
        custom_permission={
            "can_view" : self.context['request'].user.has_perm('posts.view_simplemodel'),
            "can_update" : self.context['request'].user.has_perm('change_simplemodel',obj) or self.context['request'].user.has_perm('posts.change_simplemodel'),
            "can_delete" : self.context['request'].user.has_perm('delete_simplemodel',obj) or self.context['request'].user.has_perm('posts.delete_simplemodel') ,
        }
        return custom_permission

    def get_object_level_permission(self,obj):
        post=SimpleModel.objects.get(pk=obj.id)
        return self.context['request'].user.has_perm('assign_post', post)

    def get_permission_level(self,obj):
        post=SimpleModel.objects.get(pk=obj.id)
        group = Group.objects.filter(user=self.context['request'].user)
        data=Group_Serializer(group,many=True)
        return data.data