from rest_framework import routers
from django.urls import path,include
from .views import SimpleModelViewSet,ListPosts
router = routers.SimpleRouter()
router.register(r'post-sample-view', SimpleModelViewSet)

urlpatterns = [
    path('role-based/', ListPosts.as_view()),

]

urlpatterns += router.urls

