from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser

from .serializers import UserSerializer

@extend_schema_view(
    retrieve        = extend_schema(summary = 'Retrieve a user'),
    create          = extend_schema(summary = 'Create a user'),
    update          = extend_schema(summary = 'Update a user'),
    partial_update  = extend_schema(summary = 'Partially update a user'),
    destroy         = extend_schema(summary = 'Delete a user'),
)

class UserViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def get_permissions(self):
        if self.action == 'create':
            return []
        return super().get_permissions()
