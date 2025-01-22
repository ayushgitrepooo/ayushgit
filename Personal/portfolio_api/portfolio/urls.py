from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'skill', SkillViewSet, basename='skill')


urlpatterns = [
    path("", include(router.urls)),
]

