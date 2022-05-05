from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from tools.managers import CustomUserManager

class Entity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    entity_type = models.ForeignKey('EntityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entity'

    def __str__(self):
        return self.name


class EntityType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'entity_type'

    def __str__(self):
        return self.label


class Material(models.Model):
    name = models.CharField(max_length=200)
    characteristics = models.CharField(max_length=500, blank=True, null=True)
    equipment_condition = models.CharField(max_length=100, blank=True, null=True)
    entity = models.ForeignKey(Entity, models.DO_NOTHING)
    material_type = models.ForeignKey('MaterialType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material'

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'material_type'
    
    def __str__(self):
        return self.label


class UserType(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True, null=True)

    class Meta:
        db_table = 'user_type'
    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=250, unique=True)
    id_number = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    user_type = models.ForeignKey('UserType', models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    class Meta:
        db_table = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['id_number']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserMaterial(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    material = models.ForeignKey(Material, models.DO_NOTHING)
    #request_date = models.DateTimeField(auto_now_add=False, auto_now=False)

    class Meta:
        db_table = 'user_material'

    

    