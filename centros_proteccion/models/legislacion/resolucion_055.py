from django.contrib.gis.db import models

from centros_proteccion.models import CentroAtencion, Estandarizacion
from users.models.CustomUser import UsuarioDateTime


class ResCincuentaCincoCV(UsuarioDateTime):
    """
    Caracterización según la resolución 055 de 2018, para centros vida
    """
    centro = models.ForeignKey(
        CentroAtencion,
        on_delete=models.RESTRICT,
        related_name='centros_55',
        null=False
    )
    doc_dominio = models.BooleanField(
        default=False,
        null=True,
        help_text='Documentos que acrediten el dominio del inmueble o de los derechos para se utilizados'
                  'por parte del establecimiento a traves de su representante legal'
    )
    planos_depend = models.BooleanField(
        default=False,
        null=True,
        help_text='Plano o croquis a escala de todas las dependencias'
    )
    preve_incendio = models.BooleanField(
        default=False,
        null=True,
        help_text='Prevención de incendios'
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
    cert_gas = models.BooleanField(
        default=False,
        null=True,
        help_text='Certificado de gas'
    )
    plan_evacuacion = models.BooleanField(
        default=False,
        null=True,
        help_text='Plan de evacuación'
    )
    libro_pqrs = models.BooleanField(
        default=False,
        null=True,
        help_text='Libro de PQRS'
    )


class CriteriosVidaDia(UsuarioDateTime):
    centro_proteccion = models.ForeignKey(
        CentroAtencion,
        related_name='criterios',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )

    # region talento humano
    th_director = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un director quien es responsable del cumplimiento de los servicios ofrecidos por los '
                  'centros. Deberá certificar minimo formación tecnológica o profesional en ciencias humanas, '
                  'ciencias sociales o ciencias de la salud. En centros con hasta 60 personas usuarias inscritas '
                  'cuentan con uin director o coordinador con disponibilidad de minimo 4 horas diarias por cada dia '
                  'que el centro preste servicios. En centros con 61 o mas personas usuarias inscritas cuentan con un '
                  'director o coordinador con disponibilidad de 8 horas diarias por cada dia que el centro preste '
                  'servicios.',
    )
    th_menus = models.BooleanField(
        null=False,
        default=False,
        help_text='Dispone de 1 responsable de la definición de menús del Centro,con formación en nutrición y '
                  'dietética, que garantice que laspersonas mayores reciban una alimentación variada,balanceada y '
                  'acorde a sus necesidades. En Centros con hasta 60 personas usuarias inscritas cuentan con 1 '
                  'responsable con disponibilidad de mínimo 8 horas mensuales, distribuidas en minimo 2 visitas al '
                  'mes, cada dos semanas, cada una de 4 horas continuas En Centros con 61 o más personas usuarias '
                  'inscritas cuentancon 1 responsable con disponibilidad de mínimo 16 horas mensuales, distribuidas '
                  'en mínimo 4 visitas al mes, cadasemana, cada una de 4 horas continuas',
    )
    th_mante = models.BooleanField(
        null=False,
        default=False,
        help_text='Dispone de mínimo 1 responsable del mantenimiento y aseo de la infraestructura física y '
                  'equipamiento del Centro. En Centros con hasta 15 personas usuarias inscritas cuentan con mínimo 1 '
                  'responsable con disponibilidad de mínimo 2 horas diarias por cada día que el Centro preste '
                  'servicios.  En Centros con entre 16 y 60 personas usuarias inscritas cuentan con mínimo 1 '
                  'responsable con disponibilidad de mínimo 4 horas diarias por cada dia que el Centro preste '
                  'servicios. En Centros con 61 o más personas usuarias inscritas cuentan con mínimo 1 responsable '
                  'con disponibilidad de 8 horas diarias  por cada día Que el Centro preste servicios.',
    )
    th_man_ali = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con manipulador de alimentos certificado. En Centros con hasta 15 personas usuarias '
                  'inscritas cuentan con mínimo 1 manipulador de alimentos con disponibilidad de mínimo 4 horas '
                  'diarias por cada día que el Centro preste servicios. En Centros con entre 16 y 45 personas '
                  'usuarias inscritas cuentan con mínimo 1 manipulador de alimentos con disponibilidad de mínimo 6 '
                  'horas diarias por cada día que el centro preste servicios. En Centros con entre 46 y 60 personas '
                  'usuarias inscritas cuentan con mínimo 2 manipuladores de alimentos: 1 con disponibilidad de mínimo '
                  '6 horas diarias por cada dia que el centro preste servicios y 1 con disponibilidad de mínimo 4 '
                  'horas diarias por cada día que el Centro preste servicios. En Centros con 61 o más personas '
                  'usuarias inscritas cuentan con mínimo 2 manipuladores de alimentos con disponibilidad de 8 horas '
                  'diarias cada uno por cada día que el Centro preste servicios. ',
    )
    th_aux_enf = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con mínimo técnico laboral auxiliar en enfermería o en salud pública. En Centros con hasta '
                  '60 personas usuarias inscritas cuentan con minimo 1 persona con este perfil, con disponibilidad de '
                  'mínimo el tiempo que el Centro preste servicios por cada día. En Centros con 61 o más personas '
                  'usuarias inscritas cuentan con mínimo 2 oersonas con este nerfil, con disnonibilidad de 8 horas '
                  'diarias cada una por cada día que el Centro preste servicios. ',
    )
    th_acti_fisi = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuentan con el personal mínimo para actividad física (1 persona 15 usuarios, 2 personas hasta 30 '
                  'usuarios, 3 para más usuarios y con los tiempos requeridos'
                  'por cada día que el Centro esté abierto a los usuarios para el desarrollo de los siguientes 3 '
                  'servicios en dicho periodo de tiempo: 1) actiVidades físicas y de interacción social, '
                  '2) actividades cognitivas y productivas, 3) actividades "ecreativas y culturales.',
    )
    th_cert_emergencia = models.BooleanField(
        null=False,
        default=False,
        help_text='Todo el personal del Centro cuenta con constancia o participación en formación para la atención de '
                  'emergencias, primer respondiente y manejo de elementos en emergencias de mínimo 36 horas. ',
    )
    th_cert_aten_inte = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procesos de inducción y reinducción del talento humano del Centro, orientados al '
                  'fortalecimiento de capacidades, basados en el enfoque de derechos y el modelo de atención integral '
                  'y centrada en la persona. El talento humano debe participar en estas actividades al menos una vez '
                  'al año.',

    )
    th_eval = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con evaluaciones del talento humano del Centro para determinar necesidades de mejoramiento '
                  'y calidad de las interacciones con las personas adultas mayores usuarias, sus familias, '
                  'proveedores y organizaciones de inspección,  vigilancia y control. ',
    )
    th_dir_formacion = models.BooleanField(
        null=True,
        default=False,
        help_text='El director o coordinador cuenta con constancias de asistencia o participación a formaciones para '
                  'la atención integral de personas adultas mayores. Esas formaciones deberán corresponder a un '
                  'componente teórico (presencial o virtual) de mínimo 160 horas, y a un componente de experiencia '
                  'directa de mínimo 320 horas de  atención realizadas durante o posteriormente a las formaciones. '
                  'Las anteriores constancias deben sumar un mínimo de 480 horas. Las constancia/s del componente '
                  'teórico deberá/n serexpedida/s por Instituciones de Educación para el Trabajo y el Desarrollo Humano'
                  ' o Instituciones de Educación Superior, leqalmente reconocidas por el Estado colombiano.',
    )
    th_aux_formacion = models.BooleanField(
        null=True,
        default=False,
        help_text='Elllos técnico/s laboral/es auxiliar/es en enfermería o en salud pública cuenta/n con constancia/s '
                  'de asistencia o participacióna formaCiones para la atención integral de personas adultas mayores. '
                  'Esas formaciones deberán corresponder a un componenteteórico (presencial o virtual) de mínimo 160 '
                  'horas, y a un componente de experiencia directa de mínimo 320 horas de tención realizadas durante '
                  'o posteriormente, a las formaciones. Las anteriores constancias deben sumar un mínimo de 480 '
                  'horas. La/s constancia/s del componente teórico deberá/n ser expedida/s por Instituciones de '
                  'Educación para el Trabajo y el Desarrollo Humano o Instituciones de Educación Superior, '
                  'legalmente reconocidas por el Estado colombiano.',
    )

    th_acti_recre = models.BooleanField(
        null=False,
        default=False,
        help_text='El/los responsable/s de brindar los servicios de 1) actividades físicas y de interacción social, '
                  '2) actividades cognitivas y productivas, 3) actividades recreativas y culturales cuenta/n con '
                  'constancia/s de asistencia o participación a formaciones para la atención integral de personas '
                  'adultas mayore:s. Esas formaciones deberán corresponder a un componente teórico (presencial o '
                  'virtual) de mínimo 160 horas, y a un componente de experiencia directa de mínimo 320 horas de '
                  'atención realizadas durante o posteriormente a las, formaciones. Las anteriores constancias deben '
                  'sumar un mínimo de 480 horas. la/s constancia/s del componente teorico deberá/n ser expedida/s por '
                  'Instituciones de Educación para el Trabajo y el Desarrollo Humano o Instituciones de Educación '
                  'Superior, legalmente reconocidas por el Estado colombiano.'
    )

    # region desuso
    th_proc_indu_reind_th = models.BooleanField(null=True, default=False)
    th_progr_cap_anual = models.BooleanField(null=True, default=False)
    th_acti_esti = models.BooleanField(null=True, default=False)
    # endregion

    # endregion

    # region infraestructura
    inf_ambi_limpios = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con ambientes limpios, sin malos olores, en debidas condiciones higiénico-sanitarias, '
                  'libres de ruidos y contaminacion.',
    )
    inf_ambi_solario = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con area de estar o solario, iluminado, ventilado que  permita el descanso de llos usuarios'
    )
    inf_ambi_iluminado = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un área iluminada y ventilada destinada para trabajo en grupo, compatible con '
                  'actividades de estimulación cognitiva, interacción social, lúdica, recreativa, cultural, '
                  'física y productiva. Cuenta, en cada actividad, con un área mínima en uso por usuario de 1,'
                  '5 metros2 ',
    )
    # Cambio de nombre de inf_1_5_metros a inf_3_6_metros
    inf_3_6_metros = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un ambiente para comedor destinado a la toma de los alimentos de los usuarios, '
                  'con puestos de un área mínima de 3,6 metros2.',
    )
    inf_reso_previa = models.BooleanField(
        null=False,
        default=False,
        help_text='El Centro cuenta con concepto sanitario favorable, de acuerdo con la Resolución 2674 de 2013 del '
                  'Ministerio de Salud y Protección Social o norma que la modifique o sustituya, independiente de si '
                  'los alimentos son preparados en el Centro o suministrados por proveedor,',
    )
    inf_ambiente = models.BooleanField(
        null=True,
        default=False,
        help_text='Cuenta con un área para recepción y manejo administrativo delCentro, diferente de las áreas donde '
                  'se brindan los servicios alos usuarios.',
    )
    inf_servicio_gen = models.BooleanField(
        null=True,
        default=False,
        help_text='Cuenta con área para servicios generales, con espacio destinado para el almacenamiento de '
                  'elementos de aseo, limpieza y desinfección. '
    )
    inf_deambu = models.BooleanField(
        null=True,
        default=False,
        help_text='Cuenta con áreas y ajustes razonables que permitan la movilidad segura por las instalaciones. La '
                  'edificación deberá ser accesible externa e internamente, de acuerdo con lo previsto en la '
                  'Resolución 14861 de 1985 del Ministerio de Salud o la norma Que la modifique o sustituya.'
    )
    inf_senal_emergencia = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con accesos, áreas de circulación y salidas señalizadas, de acuerdo con lo establecido en '
                  'la Resolución 14861 de 1985 del Ministerio de Salud o la norma que lo modifica o sustituya.'
    )

    inf_infra_clima = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con infraestructura acorde con las condiciones climáticas del entorno geográfico del '
                  'Centro, garantizando iluminación natural, ventilación y temperatura ajustada a las necesidades de '
                  'los usuarios.'
    )

    inf_pisos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con pisos firmes, antideslizantes y continuos y con los elementos necesarios para prevenir '
                  'caídas.'
    )

    inf_unidad_sanitaria = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con minimo 1 unidad sanitaria por sexo por cada 15 usuarios en desarrollo de las '
                  'actividades de los servicios, con facilidad de acceso para personas con discapacidad. de acuerdo '
                  'con el artículo 50 de la Resolución 14861 de 1985 del Ministerio de Salud o la norma que lo '
                  'modifica o sustituya. '
    )
    inf_ascenso = models.BooleanField(
        null=False,
        default=False,
        help_text='En instalaciones donde la atención a las personas adultas mayores se preste en más de dos pisos, '
                  'se cuenta con rampas o ascensores que cumplan criterios de accesibilidad. Además de cumplir con la '
                  'reglamentación vigente sobre escaleras y ascensores.'
    )

    # region desuso
    inf_cocina_cv = models.BooleanField(
        null=False,
        default=False,
        help_text='El servicio de cocina puede ser brindado directamente por el Centro Vida o contratado. '
                  'En el primer caso, el centro deberá contar con ambiente para recepción, almacenamiento de '
                  'víveres secos, refrigeración para víveres perecederos, despensa diaria, preparación, cocción y '
                  'distribución de alimentos con cumplimiento de licencia sanitaria para manipulación de alimentos. '
                  'También deberá disponer de área de lavado de ollas, utensilios y de vajilla, vestuarios de personas '
                  'y el área tendrá ventilación e iluminación, preferiblemente natural.'
    )

    inf_cocina_area = models.BooleanField(
        null=False,
        default=False,
        help_text='El área mínima para el servicio de cocina y según la capacidad del centro será de 1.20 metros2 por '
                  'cada usuario hasta 30 personas adultas mayores, y de 0.80 metros2 para 31 usuarios en adelante.'
    )
    inf_agua = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con dispensación de agua para las personas adultas mayores, con temperatura templada. La '
                  'dispensación de agua deberá estar libre de riesgos de quemaduras o hipotermia.'
    )

    inf_esp_acce = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con accesos, áreas de circulación y salidas señalizadas, de acuerdo con los siguientes '
                  'requisitos: 1. Especiales de accesibilidad: deberán preverse las condiciones necesarias que '
                  'permitan en cualquier espacio o ambiente interior o exterior, el fácil desplazamiento y el uso en '
                  'forma confiable y segura de los diferentes servicios, como también la fácil evacuación o salida '
                  'hacia lugares de refugio en caso de emergencia. 2. Todas las áreas de circulación general deberán '
                  'tener un ancho mínimo en todo su recorrido de 1.20 metros. 3. Se tendrá en cuenta que las puertas '
                  'no abran hacia espacios de circulación, se exceptúan puertas de entrada principal las cuales podrán '
                  'abrir en ambos sentidos.'
    )

    inf_bano = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con baño con las siguientes especificaciones: La altura de la taza del inodoro estará entre '
                  '0.45 metros y 0.50 metros del piso acabado, con barras laterales que sirvan de apoyo, localizadas a '
                  '0.35 metros por encima del aparato sanitario. Los lavamanos serán localizados de manera que su '
                  'altura máxima no exceda de 0.80 metros con espacio libre debajo de este, se debe disponer de un '
                  'asiento o mesón en el área de la ducha y el dispensador para el papel higiénico, el toallero y '
                  'las barras o agarraderas para ducha se colocarán a 0.70 metros desde el piso acabado, los espejos '
                  'estarán ubicados en su parte inferior a partir de 1.10 metros de altura con una inclinación hacia '
                  'la persona del 10%. No se podrá tener obstáculos en el piso dentro del baño.'
    )

    inf_rampas = models.BooleanField(
        null=False,
        default=False,
        help_text='Las rampas instaladas en los Centros Vida deben cumplir con los siguientes criterios: El piso de '
                  'la rampa será de material antideslizante y de textura y color diferentes a los pisos adyacentes, '
                  'este tipo de material se colocará en los descansos y antes del inicio y después de terminar la '
                  'rampa, en longitud no menor de 0.30 metros. Se deberá además cumplir con los siguientes '
                  'requisitos: 1. Tramo máximo sin descanso: 10.00 metros, con descanso entre tramos mínimo de: '
                  '1.40 metros, de profundidad. 2. Altura libre mínima en todo su recorrido: 2.20 metros. 3. Ancho '
                  'mínimo en todo su recorrido: 1.20 metros. 4. Pendiente no mayor del 11%. 5. Pasamanos a ambos '
                  'lados en todo el recorrido, uno a 0.90 metros de altura y el otro a 0.75 metros, lo cual facilita '
                  'la circulación con apoyo para las personas adultas mayores y para las personas en sillas de ruedas, '
                  'se prolongarán antes del inicio y al final, paralelos al piso: 0.30 metros, de longitud. '
                  '6. Protecciones laterales hacia espacios libres.'
    )
    # endregion desuso

    # endregion

    # region dotacion
    dot_estar_desca = models.BooleanField(
        null=True,
        default=False,
        help_text='Cuenta con equipos, muebles y elementos para ambiente de estar y descanso.',
    )
    dot_trabajo_grupo = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con equipos, insumas y elementos para área de trabajo en grupo y actividades de '
                  'estimulación cognitiva, interacciones sociales, recreativas, culturales, físicas yy-roductivas.',
    )
    dot_primer_aux = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con equipos, insumos y elementos para atención de primeros auxilios, incluida una silla de '
                  'ruedas.',
    )
    dot_bat_bano = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con insumas y elementos de aseo e higiene para baños y unidades sanitarias.',
    )
    dot_equipos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con equipos, insumas y menaje de cocina en general, acordes con la modalidad de provisión '
                  'de alimentos.',
    )
    dot_comunicacion = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con equipos, insumas y elementos para sistemas de comunicación.',
    )
    dot_residuos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cumple con la reglamentación de disposición de residuos sólidos.',
    )
    dot_cronograma = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con plan de mantenimiento de equipos, muebles y enseres.'
    )

    # region desuso
    dot_dif_mov = models.BooleanField(
        null=False,
        default=False,
        help_text='Dispone de equipamiento necesario para personas con dificultades de movilidad que facilite la mayor '
                  'independencia posible, en condiciones de seguridad.'
    )

    dot_vajilla = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con vajilla, cubertería y comedor o comedores suficientes para atender al cincuenta por '
                  'ciento (50%) de las personas adultas mayores usuarias, simultáneamente.'

    )
    # endregion desuso

    # endregion

    # region gestión
    ges_mis_vis = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con misión, visión y valores que le permitan definir sus principales líneas de desarrollo '
                  'estratégico.'
    )
    ges_procesos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procesos misionales, estratégicos y de soporte, identificados e implementados.'
    )
    ges_procedimiento = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procedimientos actualizados para llevar a cabo los procesos misionales.'
    )
    ges_proce_coordin = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con procedimiento de coordinación y articulación con el sistema de salud definido.'
    )
    ges_indicadores = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con indicadores de procesos misionales, estratégicos y de soporte cumplidos y mejorados.'
    )
    ges_sis_monitoreo = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con sistema de monitoreo para la mejora continua de los procesos.'
    )
    ges_reglamento = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con reglamento interno y manual de buen trato, elaborados con participación de las '
                  'personas adultas mayores y sus redes de apoyo.'
    )
    ges_registro = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con historias de vida y planes de atención integral y centrada en las personas adultas '
                  'mayores, cuya implementación se registra en bitácoras, debidamente archivados. '
    )
    ges_estados_financieros = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con plan anual de ejecución del presupuesto del Centro.'
    )
    # region desuso
    ges_objetivos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con objetivos relacionados con la calidad de vida de las personas adultas mayores '
                  'cumplidos y mejorados.'
    )
    ges_eval_clima = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con evaluación de clima laboral utilizada por la dirección como elemento de desarrollo '
                  'organizativo del Centro de atencion. Cuenta con plan anual de ejecución del presupuesto .'
    )
    # endregion desuso

    # endregion

    # region Valoración integral y plan personalizado de atención
    vippa_val_integral = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con valoración integral de la capacidad funcional de  cada persona adulta mayor al ingreso '
                  'al Centro que establezca su condición nutriclonal, fisica, cognitiva, psicoafectiva, social y de '
                  'historia de vida. '
    )
    vippa_ai = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con un plan de atención integral para cada usuario de los servicios del Centro.',
    )
    vippa_eval_anual = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con valoración realizada mínimo cada año sobre la  capacidad funcional de los usuarios, '
                  'para determinar cambios.',
    )
    vippa_eval_semestra = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con revisiones realizadas mínimo cada semestre a las bitácoras de los planes de atención '
                  'integral, para determinar si existen signos o síntomas que deban ser reportados al sistema de '
                  'salud. '
    )
    vippa_pai_preferencias = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con bitácoras de registro de la ejecución, seguimiento y evaluación del plan de atención '
                  'integral por cada servicio y usuario. '
    )
    # region desuso
    vippa_reg_socioecono = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con registro socioeconómico de cada una de las personas adultas mayores usuarias de la '
                  'modalidad de cuidado.'
    )
    vippa_eval_mensual = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con evaluaciones mensuales para determinar si existen síntomas depresivos, fragilidad '
                  'funcional o dolor que deba ser abordas con oportunidad.'
    )
    vippa_preferencias = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con identificación de preferencias, intereses, capacidades e historia de vida de cada una '
                  'de las personas adultas mayores usuarias del centro de atencion '
    )
    vippa_necesidad_apoyo = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con definición de necesidades de apoyo de las personas adultas mayores, valoración de '
                  'recursos formales e informales disponibles y decisiones sobre factibilidad y priorización '
                  'de intervenciones.'
    )
    vippa_registro_seguimiento = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con registro de la ejecución, seguimiento, evaluación y reprogramación del plan de atención '
                  'integral y centrado en las personas adultas mayores.'
    )
    # endregion desuso
    # endregion

    # region calidad de vida
    # region desuso
    cv_recursos = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con recursos suficientes para estimular la independencia psíquica y funcional de las '
                  'personas adultas mayores, la participación de las familias y la formación y cuidado del talento '
                  'humano del centro vida.',
    )
    cv_eval = models.BooleanField(
        null=False,
        default=False,
        help_text='El centro de atencion  dispone y aplica un procedimiento de evaluación de la calidad de vida de '
                  'cada persona adulta mayor usuaria.',
    )
    cv_resul_anuales = models.BooleanField(
        null=False,
        default=False,
        help_text='Cuenta con resultados anuales de encuestas de satisfacción o entrevistas cualitativas realizadas '
                  'a las personas adultas mayores, familiares y amigos, y talento humano del Centro Vida, por personal '
                  'diferente al que labora en el centro.',
    )
    # endregion desuso
    # endregion
    # QUESTION El campo habilitado parece estar sobrando.
    habilitado = models.BooleanField(null=True, default=False)

    # TODO estadarización n puede ser nulo
    estandarizacion = models.ForeignKey(
        Estandarizacion,
        on_delete=models.RESTRICT,
        related_name='indi_dia_vida',
        null=True
    )

    # region observaciones
    obs_general = models.TextField(null=True, blank=True)
    obv_th_director = models.TextField(null=True, blank=True)
    obv_th_aux_enf = models.TextField(null=True, blank=True)
    obv_th_cert_aten_inte = models.TextField(null=True, blank=True)
    obv_th_cert_emergencia = models.TextField(null=True, blank=True)
    obv_th_proc_indu_reind_th = models.TextField(null=True, blank=True)
    obv_th_progr_cap_anual = models.TextField(null=True, blank=True)
    obv_th_eval = models.TextField(null=True, blank=True)
    obv_th_mante = models.TextField(null=True, blank=True)
    obv_th_menus = models.TextField(null=True, blank=True)
    obv_th_man_ali = models.TextField(null=True, blank=True)
    obv_th_acti_esti = models.TextField(null=True, blank=True)
    obv_th_acti_fisi = models.TextField(null=True, blank=True)
    obv_th_acti_recre = models.TextField(null=True, blank=True)
    obv_inf_ambi_limpios = models.TextField(null=True, blank=True)
    obv_inf_ambi_solario = models.TextField(null=True, blank=True)
    obv_inf_3_6_metros = models.TextField(null=True, blank=True)
    obv_inf_cocina_area = models.TextField(null=True, blank=True)
    obv_inf_servicio_gen = models.TextField(null=True, blank=True)
    obv_inf_deambu = models.TextField(null=True, blank=True)
    obv_inf_agua = models.TextField(null=True, blank=True)
    obv_inf_infra_clima = models.TextField(null=True, blank=True)
    obv_inf_pisos = models.TextField(null=True, blank=True)
    obv_inf_unidad_sanitaria = models.TextField(null=True, blank=True)
    obv_inf_bano = models.TextField(null=True, blank=True)
    obv_inf_ascenso = models.TextField(null=True, blank=True)
    obv_inf_rampas = models.TextField(null=True, blank=True)
    obv_dot_dif_mov = models.TextField(null=True, blank=True)
    obv_dot_estar_desca = models.TextField(null=True, blank=True)
    obv_dot_primer_aux = models.TextField(null=True, blank=True)
    obv_dot_bat_bano = models.TextField(null=True, blank=True)
    obv_dot_agua = models.TextField(null=True, blank=True)
    obv_dot_vajilla = models.TextField(null=True, blank=True)
    obv_dot_comunicacion = models.TextField(null=True, blank=True)
    obv_dot_basura = models.TextField(null=True, blank=True)
    obv_dot_cronograma = models.TextField(null=True, blank=True)
    obv_ges_mis_vis = models.TextField(null=True, blank=True)
    obv_ges_procesos = models.TextField(null=True, blank=True)
    obv_ges_procedimiento = models.TextField(null=True, blank=True)
    obv_ges_proce_coordin = models.TextField(null=True, blank=True)
    obv_ges_indicadores = models.TextField(null=True, blank=True)
    obv_ges_sis_monitoreo = models.TextField(null=True, blank=True)
    obv_ges_reglamento = models.TextField(null=True, blank=True)
    obv_ges_registro = models.TextField(null=True, blank=True)
    obv_ges_objetivos = models.TextField(null=True, blank=True)
    obv_ges_eval_clima = models.TextField(null=True, blank=True)
    obv_ges_estados_financieros = models.TextField(null=True, blank=True)
    obv_vippa_reg_socioecono = models.TextField(null=True, blank=True)
    obv_vippa_val_integral = models.TextField(null=True, blank=True)
    obv_vippa_eval_mensual = models.TextField(null=True, blank=True)
    obv_vippa_preferencias = models.TextField(null=True, blank=True)
    obv_vippa_necesidad_apoyo = models.TextField(null=True, blank=True)
    obv_cv_recursos = models.TextField(null=True, blank=True)
    obv_cv_eval = models.TextField(null=True, blank=True)
    obv_cv_resul_anuales = models.TextField(null=True, blank=True)
    obv_inf_cocina_cv = models.TextField(null=True, blank=True)
    obv_inf_ambiente = models.TextField(null=True, blank=True)
    obv_inf_cocina = models.TextField(null=True, blank=True)
    obv_inf_senal_emergencia = models.TextField(null=True, blank=True)
    obv_dot_equipos = models.TextField(null=True, blank=True)
    obv_vippa_eval_semestra = models.TextField(null=True, blank=True)
    obv_vippa_registro_seguimiento = models.TextField(null=True, blank=True)
    obv_vippa_pai_preferencias = models.TextField(null=True, blank=True)
    obv_inf_ambi_iluminado = models.TextField(null=True, blank=True)
    obv_inf_esp_acce = models.TextField(null=True, blank=True)

    # region nuevos campos 20230525
    obs_th_dir_formacion = models.TextField(null=True, blank=True)
    obs_th_aux_formacion = models.TextField(null=True, blank=True)
    obs_inf_reso_previa = models.TextField(null=True, blank=True)
    obs_dot_trabajo_grupo = models.TextField(null=True, blank=True)
    obs_dot_residuos = models.TextField(null=True, blank=True)
    obs_dot_cronograma = models.TextField(null=True, blank=True)
    obs_vippa_ai = models.TextField(null=True, blank=True)
    obs_vippa_eval_anual = models.TextField(null=True, blank=True)

    # endregion nuevos campos 20230525
    # endregion observaciones

    # region sumas
    sum_th = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    sum_inf = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    sum_dot = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        null=True,
        blank=True
    )
    sum_gest = models.DecimalField(
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
    sum_cv = models.DecimalField(
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
    # endregion sumas
