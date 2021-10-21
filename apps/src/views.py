from rest_framework import generics, views, status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.src.tasks import parsing_base
from rest_framework.response import Response
from apps.src.models import Base
from apps.src.serilaizers import (
    BaseCodeSerializer, BaseSerializer
)


class BaseAPIViewSet(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class BaseCodeApiView(views.APIView):
    serializer_class = BaseCodeSerializer

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            parsing_base.delay(title=title)
            return Response(status=status.HTTP_200_OK, data={"message": "done"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "error"})
