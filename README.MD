# install django with restapi
## install libraries
create a virtual environment activate it and install django, djangoframework
```
$ pip install django
$ pip install djangorestframework
```

## create first project
```
$ django-admin startproject djswagger
$ cd djswagger
```
## go to folder and set virtualenv folder   
(macos)
```
$ setvirtualenvproject
```
(windows)
```
/> setprojectdir .
```
## create firstapp
```
python manage.py startapp hr
```
## add hr and rest_framework to settings.py
```
INSTALLED_APPS = [
	...
    'rest_framework',
    'hr',
]
```
## migrate to create db
```
./manage.py migrate
```

## create model under hr/models.py
```
class Employee(models.Model):
    id = models.IntegerField(primary_key=True,)
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id) + self.name + str(self.salary)
```

## create serializers
under hr create serializers.py
```
from rest_framework import serializers
from hr.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
```

## create your view in views.py
```
from rest_framework import viewsets
from hr.serializers import EmployeeSerializer
from hr.models import Employee

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

## urls settings
create urls.py under hr folder
```
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hr.views import EmployeeViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
go to djswagger/urls.py add the urls from hr
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hr.urls')),
]
```
## create the model in db
```
./manage.py makemigrations
./manage.py migrate
```

## check everything runs fine 
```
./manage.py runserver
```
goto url http:/localhost:8000/api

# Install swagger support
https://github.com/axnsan12/drf-yasg

## install
```
pip install drf-yasg
```
add to settings.py
```
INSTALLED_APPS = [
	...
    'rest_framework',
    'hr',
    'drf_yasg',
]
```
## add urls
in urls.py add these
```
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

## test
go to url http:/localhost:8000/swagger