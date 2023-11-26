from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crea un usuario administrador'

    def handle(self, *args, **options):
        try:
            user = get_user_model().objects.get(email='hectorpatino24@gmail.com')
        except:
            user = get_user_model().objects.create_superuser(
                email='hectorpatino24@gmail.com',
                password='contraseña123',
            )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS('Usuario administrador creado exitosamente.'))

