from django.contrib.gis.db import models

from centros_proteccion.models.base import CentroAtencion
from users.models.CustomUser import UsuarioDateTime


class LeyTreceQuince(UsuarioDateTime):
    centro = models.ForeignKey(
        CentroAtencion,
        on_delete=models.RESTRICT,
        related_name='centros_1315',
        null=False
    )
    doc_dominio = models.BooleanField(
        default=False,
        null=True,
        help_text='Documentos que acrediten el dominio del inmueble o de los derechos para ser utilizados por parte '
                  'del e establecimiento a través de su representante legal '
    )
    planos_depend = models.BooleanField(
        default=False,
        null=True,
        help_text='Plano o croquis a escala de todas las dependencias, indicando distribución de las camas y '
                  'dormitorios'
    )
    cond_sani_amb = models.BooleanField(
        default=False,
        null=True,
        help_text='Condiciones sanitarias y ambientales Ley 9 de 1979'
    )
    cert_elec = models.BooleanField(
        default=False,
        null=True,
        help_text='Certificado eléctrica'
    )
    director_tec = models.BooleanField(
        default=False,
        null=True,
        help_text='Identificación del director técnico responsable con copia de su certificado de titulo, carta de '
                  'aceptación del cargo y horario en que se encontrará en el establecimiento '
    )
    planta_personal = models.BooleanField(
        default=False,
        null=True,
        help_text='Planta del personal con que funcionará el establecimiento, con su respetivo sistema de turnos, '
                  'información que deberá actualizar-se al momento en que se produzcan cambios en este aspecto. Una '
                  'vez que entre en funciones, deberá enviar a la Secretaria de Salud competente, la nómina del '
                  'personal que labora ahí'
    )
    reg_interno = models.BooleanField(
        default=False,
        null=True,
        help_text='Reglamento interno del establecimiento, que deberá incluir un formulario de los contratos que '
                  'celebrará el establecimiento con los residentes o sus representantes, en el que se estipulen los '
                  'derechos y deberes de ambas partes y las causales de exclusión del residente'
    )
    plan_evacuacion = models.BooleanField(
        default=False,
        null=True,
        help_text='Plan de evacuación'
    )
    libro_pqrs = models.BooleanField(
        default=False,
        null=True,
        help_text='Libro foliado de uso de los residentes o sus familiares, para sugerencias o reclamos que será '
                  'timbrado por la autoridad sanitaria'
    )


class LineamientosCentroProtec(UsuarioDateTime):
    centro_proteccion = models.ForeignKey(
        CentroAtencion,
        related_name='lineamientos',
        null=True,
        blank=False,
        on_delete=models.RESTRICT
    )
    # region indicador 1 Requisitos Generales
    rg_regis_usuarios = models.BooleanField(
        null=False,
        default=False,
        help_text='La  institución  cuenta  con  el  registro  de  los  usuarios  incluyendo  los  datos mínimos  de  '
                  'identificación  de  la  persona  mayor  y  la  familia,  teléfonos  de contacto para casos de '
                  'urgencia y seguridad social en salud.',
    )
    rg_legales = models.BooleanField(
        null=False,
        default=False,
        help_text='Cumple  con  los  requisitos  legales  exigidos  por  las  normas  vigentes  con respecto a su '
                  'existencia y representación legal, de acuerdo con su naturaleza jurídica',
    )
    rg_contable = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un sistema contable para generar estados financieros según las normas contables vigentes',
    )
    rg_segurida_social = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución verifica y tiene claramente identificadas las condiciones de seguridad social en '
                  'salud de cada uno de los usuarios con el fin de coordinar los servicios de salud que deban ser '
                  'prestados fuera de ella.',
    )
    rg_encuestas = models.BooleanField(
        null=False,
        default=False,
        help_text='Aplica encuestas de satisfacción tanto a los residentes como a los familiares, las cuales incluyen '
                  'aspectos como infraestructura, trato, calidad de la comida, higiene, privacidad, actividades de '
                  'recreación, cuidados, oportunidad y participación de la familia.',
    )
    rg_pqr = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene un sistema para escuchar y tramitar las quejas y sugerencias de los residentes o sus '
                  'familiares.',
    )
    rg_situa_residente = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución evalúa la situación del residente y su familia con el fin de evitar la '
                  'institucionalización innecesaria o prematura. Aplica para los centros residenciales para persona '
                  'mayor.',
    )
    rg_crite_institu = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución cumple con los siguientes criterios de institucionalización para aceptar a un '
                  'usuario (Aplica para centros residenciales para persona mayor): Persona mayor dependiente sin '
                  'familia ni responsable conocido. Persona mayor dependiente con familia. Deberá adjuntar un '
                  'documento expreso de autorización y un documento de obligación de visita. Persona mayor '
                  'independiente sin familia. Deberá adjuntar un documento expreso de voluntad (consentimiento '
                  'informado). Persona mayor independiente con familia. Deberá adjuntar un documento expreso de '
                  'voluntad y un doc. de obligación de visita.',
    )
    rg_selecc_resi = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución cuenta con criterios de selección de residentes que pueden ingresar a la '
                  'institución y cuales no, de acuerdo con el tipo de usuarios que puede atender según su dependencia '
                  'y la capacidad de respuesta de la institución',
    )
    rg_selecc_personal = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución incluye dentro de sus procesos de selección de personal, criterios para identificar '
                  'la competencia de los trabajadores en relación con el manejo de los persona s mayores',
    )
    rg_dere_debere = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procesos documentados para capacitación en deberes y derechos dla persona Mayor, al personal '
                  'que labora en la institución',
    )
    rg_fallece = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con el procedimiento para cuando un persona mayor fallezca dentro de la institución.',
    )

    # endregion

    # region indicador 2 Servicios Habitacionales
    sh_suminis_servicios = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución garantiza los servicios de suministro de agua, energía eléctrica, sistemas de  '
                  'comunicaciones según disponibilidad tecnológica, como también de manejo y evacuación de residuos '
                  'sólidos y de residuos líquidos.',
    )
    sh_instala_agua = models.BooleanField(
        null=False,
        default=False,
        help_text='Las instalaciones interiores para suministro de agua están diseñadas y construidas de tal manera '
                  'que haya normal funcionamiento',
    )
    sh_almacena_agua = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución cuenta con tanques de almacenamiento de agua, que garantiza como mínimo, 24 horas '
                  'de servicio; y su construcción permite que durante la operación de limpieza y desinfección no se '
                  'interrumpa el suministro de agua. Tiene un área para el uso técnico de los elementos de aseo. Los '
                  'baños cuentan con los accesorios necesarios, para lavado y desinfección de patos o disponen de un '
                  'ambiente específico para este proceso. Las instituciones localizadas en zonas o ciudades de clima '
                  'frío deberán contar con calentadores de agua para el baño de los residentes.',
    )
    sh_mate_escaleras = models.BooleanField(
        null=False,
        default=False,
        help_text='Si tiene escaleras o rampas, éstas son de material antideslizante en todo su recorrido, '
                  'con pasamanos de preferencia a ambos lados, que se prolongan antes del inicio y al final, '
                  'y con protecciones laterales hacia espacios libres. En los establecimientos de más de un piso '
                  'deberán contar con un sistema seguro de traslado de los residentes entre un piso y otro ('
                  'circulación vertical) que permita la cabida de una silla de ruedas o de una camilla. '
    )
    sh_puertas_acceso = models.BooleanField(
        null=False,
        default=False,
        help_text='Las puertas de acceso a los cuartos permiten un fácil paso y giro de sillas de ruedas. El ambiente '
                  'de los baños permite el fácil desplazamiento dla persona mayor, las puertas de los baños tienen un '
                  'ancho que permite el fácil acceso de residentes en sillas de ruedas y cuentan con un sistema que '
                  'permite ser abiertas rápidamente y desde afuera. Los baños cuentan con los pasamanos necesarios '
                  'para que los residentes puedan sujetarse al hacer uso del sanitario o el lavamanos, de acuerdo con '
                  'su limitación. Los servicios higiénicos deben estar cercanos a los dormitorios, ser de fácil '
                  'acceso y estar iluminados y debidamente señalizados.',
    )
    sh_protec_areas_circ = models.BooleanField(
        null=False,
        default=False,
        help_text='Las áreas de circulación tienen protecciones laterales, en forma de baranda. Zonas de circulación '
                  'con pasillos que permitan el paso de una camilla, bien iluminados, sin desniveles o con rampas, '
                  'si los hay, y pasamanos al menos en uno de sus lados. Si tiene escaleras, estas no podrán ser de '
                  'tipo caracol no tener peldaños en abanico y deberán tener un ancho que permita el paso de dos (2) '
                  'personas al mismo tiempo, con pasamanos en ambos lados y peldaños evidenciados.',
    )
    sh_mecanis_protecc = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con mecanismos de protección contra lesiones y evita condiciones del ambiente u objetos que '
                  'puedan producir autolesiones en los persona s mayores. Incluye: '
                  'Los cables de instalación eléctrica no están en lugares de paso.'
                  'Hay interruptores para encender luces en lugares de fácil acceso, conmutados, al principio y al '
                  'final de las escaleras, en la cabecera de la cama y al principio y al final de los pasillos.'
                  'Preferiblemente con testigo luminoso para localizarlos fácilmente en la oscuridad. La institución '
                  'cuenta con buena iluminación.'
                  'Los tomacorrientes son suficientes para evitar extensiones y los que no se encuentran en uso '
                  'cuentan con protectores en caso de que haya residentes con déficit cognitivo.'
                  'Los pasamanos son de material resistente a la humedad y no conductor de electricidad'
                  'Los pisos son lisos, antideslizantes, sin elementos que sobresalgan. Si existen peldaños, '
                  'éstos están señalizados.'
                  'Los muebles están dispuestos para que no dificulten el paso; en la medida de lo posible deben '
                  'tener bordes redondeados, ser estables y resistentes y la sillas preferiblemente con brazos para '
                  'facilitar el ponerse de pie.'
                  'Los pisos de los baños son de material antideslizante o cuentan con elementos como tapetes '
                  'antideslizantes.'
                  'Los tapetes cuentan con mecanismos seguros para fijarlos al piso'
                  'Procura que los elementos para la alimentación sean difícilmente rompibles'
                  'Cuenta con un área para el almacenamiento de elementos potencialmente peligrosos con la protección '
                  'necesaria para evitar el acceso.'
                  'Cuenta con restricciones físicas para el ingreso a áreas potencialmente'
                  'peligrosas para persona s mayores con discapacidad cognitiva como cocinas, áreas de gases '
                  'medicinales, depósitos de medicamentos y almacenes de insumos, entre otras. '
                  'Procura una temperatura agradable dentro de la institución'
                  'Los pisos de estos serán antideslizantes o con aplicaciones antideslizantes, contarán con agua '
                  'caliente y fría, agarraderas de apoyo, duchas que permitan el baño auxiliado y entrada de '
                  'elementos de apoyo y timbre de tipo continuo.'
    )
    sh_progra_mantenimiento = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un programa de mantenimiento para la infraestructura de las habitaciones, baños y zonas '
                  'sociales. Zonas exteriores para recreación: patio, terraza o jardín.',
    )
    sh_dot_hospedaje = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con la dotación necesaria para brindar el servicio de hospedaje en condiciones cómodas, '
                  'seguras y adaptables a las necesidades de cada usuario. Como mínimo deberá contar con una cama y '
                  'un mueble de fácil acceso para guardar las pertenencias del usuario de manera segura. Deberá tener '
                  'algún sistema de llamado para que cada uno de los residentes pueda solicitar ayuda desde su cama y '
                  'desde el baño. Las duchas deben permitir la entrada de silla de ruedas, deberán tener un inodoro y '
                  'un lavamanos. Además habrá un lavamanos en los dormitorios de pacientes postrados.',
    )
    sh_priv_comp = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuando las habitaciones son compartidas, se cuenta con los mecanismos o procedimientos para '
                  'preservar la privacidad de los residentes.',
    )
    sh_insumos_limp = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con los insumos necesarios para la limpieza y aseo de las habitaciones, baños y zonas '
                  'sociales',
    )
    sh_vis_conv_med = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procesos documentados en relación con horarios y condiciones especiales para las visitas, '
                  'como por ejemplo normas de convivencia, manejo de medicamentos y dietas',
    )
    sh_plan_emergencia = models.BooleanField(
        null=False,
        default=False, help_text='Cuenta con planes para emergencias, desastres, seguridad e incendios.',
    )
    sh_proc_seguridad = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procesos para la seguridad de los residentes, que incluyan registros de las entradas y '
                  'salidas de cada uno de ellos y sobre la responsabilidad de custodia.',
    )
    sh_prev_enfer_infecc = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene y aplica normas de seguridad para la prevención de enfermedades infectocontagiosas.',
    )
    sh_prev_lesiones = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procedimientos preventivos de lesiones que puedan sufrir los usuarios en la institución, '
                  'previa identificación de riesgos. Deberá contar con un manual de procedimientos en el cual se '
                  'definan las normas de protección para los residentes. El manual debe incluir los procedimientos '
                  'para la supervisión permanente de los usuarios con discapacidad cognitiva en todo momento por '
                  'parte del personal de la institución, los procedimientos para la protección contra elementos o '
                  'infraestructura potencialmente riesgosos para los usuarios, los procedimientos para las '
                  'restricciones de acceso a usuarios con D.C.'
    )
    sh_proce_accidente = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procedimientos para cuando un usuario se pierda o cuando sufra algún accidente.',
    )
    sh_prev_abuso = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procedimientos documentados para prevención y manejo de abuso emocional, físico, sexual, '
                  'abandono y explotación por parte de los trabajadores de la institución u otras personas.',
    )
    sh_lavan_sergen = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con servicio de alimentación, de lavandería o ropería y servicios generales, propios o '
                  'contratados. Si no son propios, la institución debe garantizar la calidad de los procesos '
                  'contratados La cocina deberá cumplir con las condiciones higiénicas y sanitarias que aseguren una '
                  'adecuada recepción, almacenamiento, preparación y manipulación de los alimentos. Su equipamiento, '
                  'incluida la vajilla, estará de acuerdo con el número de raciones a preparar.',
    )
    sh_almac_alimentos = models.BooleanField(
        null=False,
        default=False,
        help_text='Si cuenta con cocina, existe un área para el almacenamiento de alimentos, a la cual se realiza '
                  'control de roedores e insectos El piso y las paredes serán lavables; estará bien ventilada, '
                  'ya sea directamente al exterior o a través de campana o extractor.',
    )
    sh_accid_cocina = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con la infraestructura necesaria y normas de seguridad con el fin de evitar accidentes '
                  'relacionados con la utilización de gas en la cocina, para calentamiento de agua etc.',
    )
    sh_manual_alis_nutri = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución tiene y aplica un manual de instrucción en alimentación y nutrición que incluya las '
                  'dietas especiales de los residentes de acuerdo con sus enfermedades de base, así como ciclos de '
                  'menús. Comedor o comedores suficientes para el cincuenta por ciento (50%) de los residentes '
                  'simultáneamente.',
    )
    sh_proc_varios = models.BooleanField(
        null=False,
        default=False,
        help_text='Se cuenta con procesos para la recepción, lavado, secado, planchado y almacenamiento de ropa, '
                  'si el servicio de lavandería y ropería es propio. Lugar cerrado y ventilado destinado a guardar '
                  'los útiles de aseo en uso. Una poceta para el lavado de útiles de aseo, lavadero, con un lugar de '
                  'recepción y almacenamiento para la ropa sucia, lavadora adecuada al número de residentes e '
                  'implementación para el secado y planchado de la ropa, además de un lugar para clasificar y guardar '
                  'la ropa limpia. Si existe servicio externo de lavado, se asignarán espacios para clasificar y '
                  'guardar ropa sucia y limpia.',
    )
    # endregion

    # region Indicador 3 Cuidados Persona Mayor
    cpm_cuida_capac = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con cuidadores capacitados en la atención a la persona mayor. Los cuidadores son '
                  'coordinados como mínimo por auxiliares de enfermería, los cuales también requerirán de '
                  'capacitación en el manejo de la persona mayor.',
    )
    cpm_carga_asistencial = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución ha realizado un estudio de la carga asistencial que cada residente requiere '
                  'teniendo en cuenta aspectos como: necesidades de atención, control de esfínteres, transferencias y '
                  'desplazamientos, dependencia psíquica etc, con el fin de identificar la suficiencia del recurso '
                  'humano.',
    )
    cpm_eva_bienestar = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución realiza evaluación integral de necesidades para el bienestar de la persona mayor y '
                  'desarrolla un plan integral de bienestar para cada uno de los residentes',
    )
    cpm_proc_th = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procesos documentados y aplicados en relación con la capacitación al recurso humano en '
                  'cuidado de persona mayor.',
    )
    cpm_insu_cuid_diar = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con los insumos necesarios para brindar a los usuarios los cuidados diarios relacionados '
                  'con higiene, cuidado personal y alimentación. Dormitorios con iluminación y ventilación natural, '
                  'guardarropa con espacio para cada uno de los residentes y un nochero por cama, considerando '
                  'espacio para un adecuado desplazamiento de las personas según su autonomía. Contará con un timbre '
                  'tipo continuo por habitación y en el caso de residentes postrados, uno por cama. Contar con un '
                  'número de camillas clínicas o similares para el ciento por ciento (100%) de los adultos mayores '
                  'y/o discapacitados que necesiten protección física o clínica.',
    )
    cpm_proc_activ_diarios = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene los procesos documentados en relación con las actividades diarias de los usuarios como baño, '
                  'vestido, arreglo personal, supervisión, alimentación asistida y condiciones de seguridad especial '
                  'de acuerdo con el tipo de usuarios que se encuentren en el hogar.',
    )
    cpm_proc_interven_medica = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con los procedimientos documentados para la identificación de los casos que requieren la '
                  'intervención médica y para su llamado o la valoración de la persona mayor.',
    )
    cpm_proc_cuidad_noche = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procedimientos documentados para cuidados durante la noche, servicios de relevo y '
                  'supervisión.',
    )
    cpm_proc_remision = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procesos documentados en relación con la remisión de un usuario cuando se presenten '
                  'condiciones de urgencia. Tiene identificados los mecanismos y lugares de remisión que debe atender '
                  'para cada usuario de acuerdo con su afiliación a la seguridad social.',
    )
    cpm_proc_residuos_bio = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución cuenta con procedimientos documentados para el manejo de los residuos hospitalarios '
                  'infecciosos o de riesgo biológico dispositivo hermético de almacenamiento transitorio de basura. '
                  'Todas las dependencias deberán mantenerse en buenas condiciones higiénicas.',
    )
    cpm_elem_presion = models.BooleanField(
        null=False,
        default=False,
        help_text='Para los residentes con gran inmovilidad cuenta con colchonetas o elementos para evitar las '
                  'úlceras de presión',
    )
    cpm_proc_cuidad_piel = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene documentados los procedimientos de cuidado de la piel, cambios de posición, etc. para evitar '
                  'úlceras de presión',
    )
    cpm_proc_info_familia = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene los procesos documentados en relación con la información que se da a los familiares de los '
                  'personas mayores.',
    )
    cpm_depo_medicamentos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un espacio para el depósito de medicamentos, el cual deberá estar en un área de '
                  'circulación restringida y garantiza un sistema de ventilación natural y/o artificial de forma que '
                  'conserve la vida útil de los productos farmacéuticos y afines y condiciones de temperatura y '
                  'humedad relativa, de acuerdo con lo recomendado por el fabricante. Deberá contar con la dotación '
                  'para el control de temperatura y humedad. No es obligatorio contar con servicio farmacéutico, '
                  'sin embargo si lo tiene deberá cumplir con todo lo establecido en las normas de habilitación '
                  'vigentes. Lugar cerrado para mantener equipamiento e insumos médicos y de enfermería mínimos, '
                  'tales como esfigmomanómetro, fonendoscopio, termómetros, medicamentos, elementos e insumos de '
                  'primeros auxilios y archivo de fichas clínicas.',
    )
    cpm_proc_riesgo_servicio = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución realiza procesos de evaluación y seguimiento de los riesgos inherentes al servicio, '
                  'tales como: No. de Infecciones intrainstitucionales al mes, No. de caídas al mes, No. de otros '
                  'accidentes al mes, No. de complicaciones de los procedimientos que se realizan en la institución '
                  'al mes.',
    )
    cpm_ss_decreto = models.BooleanField(
        null=False,
        default=False,
        help_text='Si ofrece servicios de salud, cumple con lo establecido en el Decreto 1011 de 2006 y la Resolución '
                  '1043 de 2006 o las normas que lo modifiquen, adicionen o sustituyan.',
    )
    cpm_ss_plan_individual = models.BooleanField(
        null=False,
        default=False,
        help_text='Si ofrece servicios de salud, la institución desarrolla un plan individual para el manejo de cada '
                  'uno de los usuarios, por parte de los profesionales de salud que participen en su tratamiento, '
                  'coordinado por un médico, el cual incluya las actividades a realizar y su periodicidad en especial '
                  'lo relacionado con visita médica, exámenes de control, medicamentos, procedimientos, supervisión y '
                  'dietas.',
    )
    cpm_ss_proc_prescripcion = models.BooleanField(
        null=False,
        default=False,
        help_text='Si tiene servicios de salud, cuenta con procedimientos para la prescripción y realización de '
                  'ejercicio, en especial para los usuarios que presenten patologías crónicas y/o rehabilitación. La '
                  'prescripción del ejercicio solo podrá ser realizada por médico o fisioterapeuta',
    )
    # endregion

    # region Indicador 4 Asesoría y educación
    sae_proc_activ_educ = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene documentados los procedimientos para las actividades educativas y de programas laborales '
                  'para la enseñanza de nuevos oficios, de acuerdo con el estado y preferencia de cada usuario. Si se '
                  'desarrollan actividades preventivas por parte de los persona s mayores, se establece con claridad '
                  'la destinación de los recursos obtenidos '
    )
    sae_proc_apoyo_familia = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene documentados los procesos para apoyar a la familia de los usuarios con demencia o '
                  'discapacidad cognitiva. '
    )

    sae_proc_deb_der_usuario = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene procesos documentados para capacitación en deberes y derechos a los usuarios y sus familias '
                  'cuenta con al menos una oficina/sala de recepción, que permita mantener entrevistas en forma '
                  'privada con los residentes y sus familiares.'
    )

    sae_proc_visitas = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procesos para estimular las visitas e integrar a la familia de los residentes y evitar '
                  'el abandono. Aplica para los centros residenciales para persona mayor.'
    )

    sae_proc_vida_saludable = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procedimientos documentados para estimular y fortalecer hábitos de vida saludable para '
                  'la persona mayor como por ejemplo: ,Promoción de autonomía e independencia, Realización de '
                  'ejercicio físico en forma regular, Combatir la obesidad, Disminuir el consumo de alcohol y '
                  'tabaco, Evitar ropas ajustadas, Uso de calzado adecuado, Evita situaciones de estrés, Tomar '
                  'medidas que prevengan las malas posturas, Cuidados de los pies, Uso de cremas hidratantes'
                  'No exposiciones prolongadas al sol, Estimular el consumo de alimentos frescos en lugar de '
                  'los que contienen conservantes y preservativos, Participar en las actividades lúdicas o culturales, '
                  'Expresar su sexualidad, Estimular la capacidad de expresar sentimientos, Estimular la '
                  'aceptación de las limitaciones y mejoramiento de autoimagen'
    )
    # endregion

    # region Indicador 5 Recreación y Socialización
    rs_esp_ludico = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un espacio físico de usos múltiples que en conjunto, tengan capacidad para contener a '
                  'todos los residentes en forma simultánea. Estas deberán tener iluminación natural, '
                  'medios de comunicación con el mundo exterior y elementos de recreación para los residentes, '
                  'tales como música, juegos, revistas, libros, etc.'
    )
    rs_prog_acti_recre = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene un programa documentado para las actividades recreativas como por ejemplo: Juegos de mesa. '
                  'Deportes para la persona mayor. Tratamientos de relajación. Danza. Biblioteca. '
                  'Actividades culturales. Manualidades. Jardinería. Paseos turísticos guiados. '
                  'Convivencias. Reinserción familiar. Actividades económicas y productivas. '
                  'Para la ejecución del programa se deberá tener en cuenta las condiciones, habilidades, '
                  'preferencias y cultura de cada uno de los usuarios.'
    )
    rs_dot_ludicos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con la dotación de elementos lúdicos y de recreación definidos por la institución'
    )
    rs_serv_religioso = models.BooleanField(
        null=False,
        default=False,
        help_text='Tiene facilidades para que los residentes tengan acceso a servicios religiosos. '
                  'Aplica para los centros residenciales para persona mayor'
    )
    rs_parti_voluntaria = models.BooleanField(
        null=False,
        default=False,
        help_text='La institución identifica las acciones de participación voluntaria en las actividades diarias '
                  'de la institución, en cada uno de los residentes de acuerdo con sus habilidades y capacidades '
                  'físicas y cognitivas'
    )
    # endregion

    # TODO este valor no puede ser nulo
    estandarizacion = models.ForeignKey(
        Estandarizacion,
        on_delete=models.RESTRICT,
        related_name='indi_proteccion',
        null=True,
        blank=True

    )
    # region observaciones
    obs_general = models.TextField(null=True, blank=True)
    obv_regis_usuarios = models.TextField(null=True, blank=True)
    obv_requi_legales = models.TextField(null=True, blank=True)
    obv_sis_contable = models.TextField(null=True, blank=True)
    obv_verif_segurida_social = models.TextField(null=True, blank=True)
    obv_apli_encuestas = models.TextField(null=True, blank=True)
    obv_pqr = models.TextField(null=True, blank=True)
    obv_situa_residente = models.TextField(null=True, blank=True)
    obv_crite_institu = models.TextField(null=True, blank=True)
    obv_selecc_resi = models.TextField(null=True, blank=True)
    obv_selecc_personal = models.TextField(null=True, blank=True)
    obv_procesos_dere_debere = models.TextField(null=True, blank=True)
    obv_proce_fallece = models.TextField(null=True, blank=True)
    obv_suminis_servicios = models.TextField(null=True, blank=True)
    obv_instala_agua = models.TextField(null=True, blank=True)
    obv_almacena_agua = models.TextField(null=True, blank=True)
    obv_mate_escaleras = models.TextField(null=True, blank=True)
    obv_puertas_acceso = models.TextField(null=True, blank=True)
    obv_protec_areas_circ = models.TextField(null=True, blank=True)
    obv_mecanis_protecc = models.TextField(null=True, blank=True)
    obv_progra_mantenimiento = models.TextField(null=True, blank=True)
    obv_dotacion_hospedaje = models.TextField(null=True, blank=True)
    obv_privacidad_compartida = models.TextField(null=True, blank=True)
    obv_insumos_limpieza = models.TextField(null=True, blank=True)
    obv_documentos_vis_conv_med = models.TextField(null=True, blank=True)
    obv_plan_emergencia = models.TextField(null=True, blank=True)
    obv_procesos_seguridad = models.TextField(null=True, blank=True)
    obv_preven_enfer_infecc = models.TextField(null=True, blank=True)
    obv_preven_lesiones = models.TextField(null=True, blank=True)
    obv_procediminetos_accidente = models.TextField(null=True, blank=True)
    obv_preven_abuso = models.TextField(null=True, blank=True)
    obv_servicios_ali_lavan_sergen = models.TextField(null=True, blank=True)
    obv_almacenamiento_alimentos = models.TextField(null=True, blank=True)
    obv_accid_cocina = models.TextField(null=True, blank=True)
    obv_manual_alis_nutri = models.TextField(null=True, blank=True)
    obv_procesos_varios = models.TextField(null=True, blank=True)
    obv_cuidador_capacitado = models.TextField(null=True, blank=True)
    obv_carga_asistencial = models.TextField(null=True, blank=True)
    obv_evalucion_bienestar = models.TextField(null=True, blank=True)
    obv_proc_th = models.TextField(null=True, blank=True)
    obv_insumos_cuidados_diarios = models.TextField(null=True, blank=True)
    obv_proc_activ_diarios = models.TextField(null=True, blank=True)
    obv_proc_interven_medica = models.TextField(null=True, blank=True)
    obv_proc_cuidad_noche = models.TextField(null=True, blank=True)
    obv_proc_remision = models.TextField(null=True, blank=True)
    obv_proc_residuos_bio = models.TextField(null=True, blank=True)
    obv_elem_presion = models.TextField(null=True, blank=True)
    obv_proc_cuidad_piel = models.TextField(null=True, blank=True)
    obv_proc_info_familia = models.TextField(null=True, blank=True)
    obv_depo_medicamentos = models.TextField(null=True, blank=True)
    obv_proc_riesgo_servicio = models.TextField(null=True, blank=True)
    obv_ss_decreto = models.TextField(null=True, blank=True)
    obv_ss_plan_individual = models.TextField(null=True, blank=True)
    obv_ss_proc_prescripcion = models.TextField(null=True, blank=True)
    obv_proc_activ_educativas = models.TextField(null=True, blank=True)
    obv_proc_apoyo_familia = models.TextField(null=True, blank=True)
    obv_proc_deb_der_usuario = models.TextField(null=True, blank=True)
    obv_proc_visitas = models.TextField(null=True, blank=True)
    obv_proc_vida_saludable = models.TextField(null=True, blank=True)
    obv_esp_ludico = models.TextField(null=True, blank=True)
    obv_prog_acti_recre = models.TextField(null=True, blank=True)
    obv_dot_ludicos = models.TextField(null=True, blank=True)
    obv_serv_religioso = models.TextField(null=True, blank=True)
    obv_parti_voluntaria = models.TextField(null=True, blank=True)

    # endregion

    # region sumatorias
    suma_rg = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    suma_sh = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    suma_cpm = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    suma_sae = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    sum_eva = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    suma_rs = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    suma_total = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    # endregion
