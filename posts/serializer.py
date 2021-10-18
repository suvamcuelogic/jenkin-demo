from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import SimpleModel
from guardian.shortcuts import assign_perm

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
    permission_by_gurdian_user_wise = serializers.SerializerMethodField()
    class Meta:
        model = SimpleModel
        fields = ["author","title","description","status","datetime","permission_crud","permission_by_gurdian_user_wise"]

    def get_permission_crud(self,obj):
        custom_permission={
            "can_view" : self.context['request'].user.has_perm('posts.view_simplemodel'),
            "can_update" : self.context['request'].user.has_perm('change_simplemodel',obj) or self.context['request'].user.has_perm('posts.change_simplemodel'),
            "can_delete" : self.context['request'].user.has_perm('delete_simplemodel',obj) or self.context['request'].user.has_perm('posts.delete_simplemodel') ,
        }
        return custom_permission

    def get_permission_by_gurdian_user_wise(self,obj):
        post=SimpleModel.objects.get(pk=obj.id)
        return self.context['request'].user.has_perm('assign_post', post)