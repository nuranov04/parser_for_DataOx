from django.urls import path
from apps.src.views import BaseAPIViewSet, BaseCodeApiView

urlpatterns = [
    path('', BaseAPIViewSet.as_view(), name='index'),
    path('title/', BaseCodeApiView.as_view(), name='title')
]

