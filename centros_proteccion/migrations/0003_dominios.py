from django.db import migrations


def crear_dominios(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    condicion = ['Público', 'Privado', 'Mixto']
    concepto_sanitario = ['Favorable', 'Desfavorable', 'Sin concepto', 'Pendiente']
    servicios_salud = ['Medicina', 'Terapia Ocupacional', 'Terapia Física', 'Terapia Respiratoria',
                       'Enfermería', 'Sicología', 'Geriatría', 'Gerontología', 'Nutricion',
                       'Otros']
    servicios_internos = ['Alojamiento', 'Alimentación', 'Lavandería', 'Cuidado Integral', 'Recreación',
                          'Salidas', 'Trabajo Social']
    administracion = ['Iglesia', 'Alcaldía', 'Departamento', 'Independiente', 'Operador']
    area = ['Urbano', 'Rural']
    tipo_persona = ['Natural', 'Jurídica']
    condicion_model = apps.get_model('centros_proteccion', 'DCondicion')
    concepto_sanitario_model = apps.get_model('centros_proteccion', 'DConceptoSanitario')
    servicios_salud_model = apps.get_model('centros_proteccion', 'DServiciosSalud')
    servicios_internos_model = apps.get_model('centros_proteccion', 'DServicios')
    administracion_model = apps.get_model('centros_proteccion', 'DAdministrador')
    tipo_persona_model = apps.get_model('centros_proteccion', 'DTipoPersona')
    area_model = apps.get_model('centros_proteccion', 'DArea')
    for condicion_nombre in condicion:
        condicion_model.objects.using(db_alias).create(nombre=condicion_nombre)
    for concepto_sanitario_nombre in concepto_sanitario:
        concepto_sanitario_model.objects.using(db_alias).create(nombre=concepto_sanitario_nombre)
    for servicios_salud_nombre in servicios_salud:
        servicios_salud_model.objects.using(db_alias).create(nombre=servicios_salud_nombre)
    for servicios_internos_nombre in servicios_internos:
        servicios_internos_model.objects.using(db_alias).create(nombre=servicios_internos_nombre)
    for administracion_nombre in administracion:
        administracion_model.objects.using(db_alias).create(nombre=administracion_nombre)
    for area_nombre in area:
        area_model.objects.using(db_alias).create(nombre=area_nombre)
    for tipo_persona_nombre in tipo_persona:
        tipo_persona_model.objects.using(db_alias).create(nombre=tipo_persona_nombre)


class Migration(migrations.Migration):

    dependencies = [
        ('centros_proteccion', '0002_rename_provicia_municipio_provincia'),
    ]

    operations = [
        migrations.RunPython(crear_dominios),
    ]
