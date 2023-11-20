from users.models.CustomUser import UsuarioDateTime


class AbstractCaracterizacion(UsuarioDateTime):
    class Meta:
        abstract = True
        permissions = (
            ('ver_caracterizacion', 'Puede ver la caracterización'),
            ('modificar_caracterizacion', 'Puede modificar la caracterización'),
            ('crear_caracterizacion', 'Puede crear la caracterización'),
            ('eliminar_caracterizacion', 'Puede eliminar la caracterización'),
        )
