from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, AttendenceViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('studentapi', StudentViewSet)
router.register('api', AttendenceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
