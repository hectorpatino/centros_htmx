from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.gis.db import models
from django.db import models
from django.contrib.auth.models import Group


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email no puede estar vacío")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email=email, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["email"]


class GroupDetails(models.Model):
    group = models.OneToOneField(Group, on_delete=models.RESTRICT)
    code = models.CharField(max_length=4)
    description = models.TextField()


class UsuarioDateTime(models.Model):
    creado = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    actualizado = models.DateTimeField(
        null=True
    )
    usuario_registro = models.ForeignKey(
        get_user_model(),
        on_delete=models.RESTRICT,
        null=False
    )

    def save(self, *args, **kwargs):
        if 'request' in kwargs:
            self.usuario_registro = kwargs.pop('request').user
        else:
            user = None
        if not self.usuario_registro:
            self.usuario_registro = user

        super(UsuarioDateTime, self).save(*args, **kwargs)

    class Meta:
        abstract = True
