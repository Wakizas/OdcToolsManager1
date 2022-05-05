from rest_framework.viewsets import ModelViewSet

from tools.models import Material, MaterialType, Entity, EntityType, UserType, User, UserMaterial

from tools.serializers import MaterialSerializer, MaterialTypeSerializer, EntitySerializer, EntityTypeSerializer, UserTypeSerializer, UserSerializer, UserMaterialSerializer


class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        materials = Material.objects.all()
        return materials


class MaterialTypeViewSet(ModelViewSet):
    serializer_class = MaterialTypeSerializer

    def get_queryset(self):
        materials = MaterialType.objects.all()
        return materials


class EntityViewSet(ModelViewSet):
    serializer_class = EntitySerializer

    def get_queryset(self):
        entity = Entity.objects.all()
        return entity


class EntityTypeViewSet(ModelViewSet):
    serializer_class = EntityTypeSerializer

    def get_queryset(self):
        entity = EntityType.objects.all()
        return entity

class UserTypeViewSet(ModelViewSet):

    serializer_class = UserTypeSerializer
    
    def get_queryset(self):
        users_types = UserType.objects.all()
        return users_types


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    
    def get_queryset(self):
        users = User.objects.all()
        return users


class UserMaterialViewSet(ModelViewSet):

    serializer_class = UserMaterialSerializer
    
    def get_queryset(self):
        requests = UserMaterial.objects.all()
        return requests