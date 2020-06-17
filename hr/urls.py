from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hr.views import EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]