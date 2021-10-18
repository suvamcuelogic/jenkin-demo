from rest_framework import routers
from django.urls import path,include
from .views import SimpleModelViewSet,ListPosts,ListPosts2
router = routers.SimpleRouter()
router.register(r'post-sample-view', SimpleModelViewSet)

urlpatterns = [
    path('role-based/', ListPosts.as_view()),
    path('role-based-view/', ListPosts2.as_view()),


]

urlpatterns += router.urls

