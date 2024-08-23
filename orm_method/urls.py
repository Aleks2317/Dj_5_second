from django.urls import path
from orm_method.views import index


urlpatterns = [
    path('', index, name='index')
]
