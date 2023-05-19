# -------Lista de lisbrerias y Modulos
try:

    # ---------------LIBRERIAS DE FECHA Y HORA
    import datetime
    import copy

    # Tipo de dato decimal
    import decimal
    from app_Abstract.atributosAbstract import AtributosSucerp, AtributosGx

    from app_Config.config import ConfigurarAplicacion
    import pyodbc
    from pydal.adapters.db2 import DB2Pyodbc


    # --------------LIBRERIA PYDAL
    # --- PARA LA DEFINICION DE TABLAS Y LOS CAMPOS DE ELLAS
    from pydal import DAL, Field
    from pydal.objects import Table

except Exception as e:
    print(f'Falta algun modulo {e}')

"""
Son los Tipos de datos  y referencias para capa abstracta
    este es otro ejemplo
types = {
    'boolean': 'CHAR(1)',
    'string': 'VARCHAR(%(length)s)',
    'text': 'CLOB',
    'json': 'CLOB',
    'password': 'VARCHAR(%(length)s)',
    'blob': 'BLOB',
    'upload': 'VARCHAR(%(length)s)',
    'integer': 'INT',
    'bigint': 'BIGINT',
    'float': 'REAL',
    'double': 'DOUBLE',
    'decimal': 'NUMERIC(%(precision)s,%(scale)s)',
    'date': 'DATE',
    'time': 'TIME',
    'datetime': 'TIMESTAMP',
    'id': 'INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'reference': 'INT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'list:integer': 'CLOB',
    'list:string': 'CLOB',
    'list:reference': 'CLOB',
    'big-id': 'BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'big-reference': 
        'BIGINT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference FK': 
        ', CONSTRAINT FK_%(constraint_name)s 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference TFK': 
        ' CONSTRAINT FK_%(foreign_table)s_PK 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_table)s (%(foreign_key)s) ON DELETE %(on_delete_action)s',
    }
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder obtener el diccionario de un Objeto Tabla
class ToolsAbatract():
    """
    El objetivo de esta clase es poder recuperar los elmentos para poder gestionar las bases de datos:\n
        La key  de una tabla\n
        El registro a actualizar\n
        Los campos de la estructura de la Tabla\n
        Almacenado en gestion_Tablas_dict\n
    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor
    def __init__(self):

        # Tabla
        self.__tabla = None

        # Campos del Mensaje
        self.__key = dict()
        self.__registro = dict()
        self.__campos = dict()

        # Gestion de las Tablas
        self.__gestion_Tablas_dict = dict()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos

    # ----------DETERMINA EL CAMPOS ID DE LA TABLA--------------------------------
    # getter del atributo objeto tabla
    @property
    def tabla(self):
        return self.__tabla

    # setter del atributo objeto tabla
    @tabla.setter
    def tabla(self, valor):
        self.__tabla = valor
        self.__id_Tabla = self.__tabla._id.longname
        self.__id_Tabla = self.__id_Tabla[(self.__id_Tabla.find('.') + 1):]

    # ----------CAMPOS DE LA TABLAS--------------------------------
    # getter del atributo campos
    @property
    def campos(self):
        return self.__campos

    # setter del atributo campos
    @campos.setter
    def campos(self, valor):
        campos = valor
        for c in campos:
            if c != self.__id_Tabla:
                self.__campos[c] = None

    # ----KEY DE LAS TABLAS------------------------
    # getter del atributo key
    @property
    def key(self):
        return self.__key

    # setter del atributo key
    @key.setter
    def key(self, valor):
        self.__key = valor

    # ----REGISTRO DE LAS TABLAS------------------------
    # getter del atributo registro
    @property
    def registro(self):
        return self.__registro

    # setter del atributo registro
    @registro.setter
    def registro(self, valor):
        self.__registro = valor

    # ----MENSAJE INSERT------------------------
    # getter del atributo mensaje_insert
    @property
    def mensaje_insert(self):
        self.__mensaje_insert = {'datos': self.registro}
        return self.__mensaje_insert

    # ----GESTION TABLAS------------------------
    # getter del atributo gestion_Tablas_dict
    @property
    def gestion_Tablas_dict(self):
        return self.__gestion_Tablas_dict

    # setter del atributo gestion_Tablas_dict
    @gestion_Tablas_dict.setter
    def gestion_Tablas_dict(self, valor):
        self.__gestion_Tablas_dict = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtiene el diccionario de manejo de la tabla
    def getTableTools(self, tabla):

        """"
        tabla = Es el objeto tabla
        retorna un diccionario con los elementos de la tabla
        """

        # determinamos si el objeto es de tipo Tabla    
        if type(tabla) is Table:

            # asignamos el objeto tabla
            self.tabla = tabla

            #  asignamos el atributo los campos de la tabla
            self.campos = tabla.fields()

            # asignamos los atributos key, registros
            self.key, self.registro = {self.__id_Tabla: None}, self.campos

            self.gestion_Tablas_dict[tabla._id.tablename] = dict()

            #  asignamos los items para el diccionario 
            self.gestion_Tablas_dict[tabla._id.tablename]['table'] = tabla
            self.gestion_Tablas_dict[tabla._id.tablename]['campos'] = self.campos
            self.gestion_Tablas_dict[tabla._id.tablename]['insert'] = self.mensaje_insert
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key, 'registro': self.registro}
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key}
            return self.gestion_Tablas_dict

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder describir los campos de cada tabla que 
# estan en motor SQLITE
class SqliteAbstractDb():

    # Constructor
    def __init__(self, db):

        """
        db = Objeto de conexion
        retorna una instancia de la clase
        """

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas del Validator
        self.__mensajesError = None
        self.__mensajesErrorMsgdDinamicos = None
        self.__msgNivelGravedad = None
        self.__userPathFile = None
        self.__usuario = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----USERPATHFILE
    #     FOR SYSTEM NAME USERP00001------------------------
    # setter del atributo privado __userPathFile
    @property
    def sq_userPathFile_Dal(self):

        # si no esta asignado el atributo
        if self.__userPathFile is None:
            try:
                self.__userPathFile = self.db.define_table(
                    'USERPATHFILE',
                    Field('USERPATHFILEID', type='id', label='Id'),
                    Field('USERNAME', type='string', length=10, required=True, label='Nombre Usuario'),
                    Field('USERPATHFILEMODULO', type='string', length=50, required=True, label='Modulo del Usuario'),
                    Field('USERPATHFILEPATH', type='string', length=50, required=True, label='Path de Files'),
                    Field('USEROUTPUT', type='string', length=1, required=True, label='OutPut'),
                    Field('USERLINKPROD', type='string', length=512, required=True, label='User Link Prod'),
                    Field('USERLINKTEST', type='string', length=512, required=True, label='User Link Test'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__userPathFile

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    # setter del atributo privado __msgNivelGravedad
    @property
    def sq_msgNivelGravedad_Dal(self):

        # si no esta asignado el atributo
        if self.__msgNivelGravedad is None:
            try:
                self.__msgNivelGravedad = self.db.define_table(
                    'MSGNIVELGRAVEDAD',
                    Field('NIVELGRAVEDADID', type='id', label='Id'),
                    Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50, required=True, label='Descripcion'),
                    Field('MSGNIVELGRAVEDADALERTA', type='string', length=50, required=True, label='Ayuda Mensaje'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__msgNivelGravedad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    # setter del atributo privado __mensajesError
    @property
    def sq_mensajeError_Dal(self):

        # si no esta asignado el atributo
        if self.__mensajesError is None:
            try:
                self.__mensajesError = self.db.define_table(
                    'MENSAJESERROR',
                    Field('MSGCODE', type='string', length=7, required=True, label='Mensaje Codigo'),
                    Field('MSGDESCRIPCION', type='string', length=150, required=True, label='Descripcion'),
                    Field('MSGHELP', type='string', length=1024, required=True, label='Ayuda Mensaje'),
                    Field('NIVELGRAVEDADID', 'reference MSGNIVELGRAVEDAD', label='Id', ondelete='CASCADE'),
                    primarykey=['MSGCODE'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesError

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    # setter del atributo privado
    @property
    def sq_mensajesErrorMsgdDinamicos_Dal(self):

        # si no esta asignado el atributo
        if self.__mensajesErrorMsgdDinamicos is None:
            try:
                self.__mensajesErrorMsgdDinamicos = self.db.define_table(
                    'MENSAJESERRORMSGDINAMICOS',
                    Field('MSGCODE', type='integer', required=True, label='Codigo del Mensaje'),
                    Field('MSGDINAMICOID', type='integer', required=True, label='Mensaje Dinamico Id'),
                    Field('MSGDINAMICOLEN', type='integer', required=True, label='Ayuda Mensaje'),
                    primarykey=['MSGCODE', 'MSGDINAMICOID'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesErrorMsgdDinamicos

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# clase que maneja las tablas del esquema GxProd
class GxAbstractDb():
    """
    EL OBJTIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE LAS TABLAS QUE ESTAN EN EL MOTOR ISERIES O MYSQL \n
    EN EL CASO DEL ISERIES LAS TABLAS ESTAN EN LA BIBLIOTECA GXPROD O GXTST DE ACUERDO A LA CONFIGURACION \n
    CUANDO TRABAJAMOS SIN CONEXION A LA ISERIES SE TRABAJA CON MYSQL \n

    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor
    def __init__(self, db):

        """
        db = Objeto de conexion
        retorna una instancia de la clase
        """

        # Conexion
        self.db = db

        # Formatos
        self.formatosSucerp = AtributosSucerp()
        self.formatosGx = AtributosGx()

        # diccionario de objetos tablas
        self.__GxdictObjetosTablas = dict()


        # ------------------------------------------------------
        # Tablas de GxProd

        self.__tipoRegistro = None
        self.__tipoSubRegistro = None
        self.__tipoCuerpo = None
        self.__tipoTitular = None
        self.__tipoOrigen = None
        self.__tipoMovimiento = None
        self.__tipoCuota = None
        self.__tipoPago = None
        self.__tipoMoneda = None
        self.__tipoDocumento = None
        self.__provincias = None
        self.__estado = None
        self.__encabezado = None

        self.__registroEncabezado = None
        self.__altaImpositiva = None
        self.__altaImpositivaTitular = None
        self.__bajaImpositiva = None
        self.__bajaImpositivaTitular = None
        self.__impuestoSellos = None
        self.__impuestoSellosPartes = None
        self.__impuestoSellosPartesTipoTramite = None
        self.__impuestoAutomotor = None

        self.__informacionVehiculo = None
        self.__informacionVehiculoTitular = None
        self.__cambioTitularidad = None
        self.__cambioTitularidadTitular = None
        self.__informacionRadicacion = None
        self.__anulacionTramitesSellos = None
        self.__anulacionTramitesSellosDetalle = None
        self.__tramitesGenerales = None
        self.__tramitesGeneralesTitular = None
        self.__pie = None

        self.__apiAumoso = None
        self.__apiToken = None
        self.__apiTokenUser = None
        self.__apiTokenUserRef = list()
        self.__apiRegistros = None
        self.__apiEstados = None
        self.__apiTareas = None
        self.__apiEstadosTareas = None
        self.__relArbaSucerpMarca = None
        self.__procesoImportacionExportacion = None
        self.__apiLog = None


        self.__tmpInformacionVehiculo = None
        self.__tmpInformacionVehiculoTitular = None

    # ----Atributos------------------------
    #@property
    #def encabezado(self):
    #    return self.__encabezado

    #@encabezado.setter
    #def encabezado(self, valor):
    #    self.__encabezado = valor

    # getter del atributo tipoRegistro
    @property
    def tipoRegistro(self):
        return self.__tipoRegistro

    # setter del atributo tipoRegistro
    @tipoRegistro.setter
    def tipoRegistro(self, valor):
        self.__tipoRegistro = valor

    # getter del atributo tipoSubRegistro
    @property
    def tipoSubRegistro(self):
        return self.__tipoSubRegistro

    # setter del atributo tipoSubRegistro
    @tipoSubRegistro.setter
    def tipoSubRegistro(self, valor):
        self.__tipoSubRegistro = valor

    # getter del atributo tipoCuerpo
    @property
    def tipoCuerpo(self):
        return self.__tipoCuerpo

    # setter del atributo tipoCuerpo
    @tipoCuerpo.setter
    def tipoCuerpo(self, valor):
        self.__tipoCuerpo = valor

    # getter del atributo tipoTitular
    @property
    def tipoTitular(self):
        return self.__tipoTitular

    # setter del atributo tipoTitular
    @tipoTitular.setter
    def tipoTitular(self, valor):
        self.__tipoTitular = valor

    # getter del atributo tipoOrigen
    @property
    def tipoOrigen(self):
        return self.__tipoOrigen

    # setter del atributo tipoOrigen
    @tipoOrigen.setter
    def tipoOrigen(self, valor):
        self.__tipoOrigen = valor

    # getter del atributo tipoMovimiento
    @property
    def tipoMovimiento(self):
        return self.__tipoMovimiento

    # setter del atributo tipoMovimiento
    @tipoMovimiento.setter
    def tipoMovimiento(self, valor):
        self.__tipoMovimiento = valor

    # getter del atributo tipoCuota
    @property
    def tipoCuota(self):
        return self.__tipoCuota

    # setter del atributo tipoCuota
    @tipoCuota.setter
    def tipoCuota(self, valor):
        self.__tipoCuota = valor

    # getter del atributo tipoPago
    @property
    def tipoPago(self):
        return self.__tipoPago

    # setter del atributo tipoPago
    @tipoPago.setter
    def tipoPago(self, valor):
        self.__tipoPago = valor

    # getter del atributo tipoMoneda
    @property
    def tipoMoneda(self):
        return self.__tipoMoneda

    # setter del atributo tipoMoneda
    @tipoMoneda.setter
    def tipoMoneda(self, valor):
        self.__tipoMoneda = valor

    # getter del atributo tipoDocumento
    @property
    def tipoDocumento(self):
        return self.__tipoDocumento

    # setter del atributo tipoDocumento
    @tipoDocumento.setter
    def tipoDocumento(self, valor):
        self.__tipoDocumento = valor

    # getter del atributo provincias
    @property
    def provincias(self):
        return self.__provincias

    # setter del atributo provincias
    @provincias.setter
    def provincias(self, valor):
        self.__provincias = valor

    # getter del atributo estado
    @property
    def estado(self):
        return self.__estado

    # setter del atributo estado
    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    # getter del atributo registroEncabezado
    @property
    def registroEncabezado(self):
        return self.__registroEncabezado

    # setter del atributo registroEncabezado
    @registroEncabezado.setter
    def registroEncabezado(self, valor):
        self.__registroEncabezado = valor

    # getter del atributo altaImpositiva
    @property
    def altaImpositiva(self):
        return self.__altaImpositiva

    # setter del atributo altaImpositiva
    @altaImpositiva.setter
    def altaImpositiva(self, valor):
        self.__altaImpositiva = valor

    # getter del atributo altaImpositivaTitular
    @property
    def altaImpositivaTitular(self):
        return self.__altaImpositivaTitular

    # setter del atributo altaImpositivaTitular
    @altaImpositivaTitular.setter
    def altaImpositivaTitular(self, valor):
        self.__altaImpositivaTitular = valor

    # getter del atributo bajaImpositiva
    @property
    def bajaImpositiva(self):
        return self.__bajaImpositiva

    # setter del atributo bajaImpositiva
    @bajaImpositiva.setter
    def bajaImpositiva(self, valor):
        self.__bajaImpositiva = valor

    # getter del atributo bajaImpositivaTitular
    @property
    def bajaImpositivaTitular(self):
        return self.__bajaImpositivaTitular

    # setter del atributo bajaImpositivaTitular
    @bajaImpositivaTitular.setter
    def bajaImpositivaTitular(self, valor):
        self.__bajaImpositivaTitular = valor

    # getter del atributo impuestoSellos
    @property
    def impuestoSellos(self):
        return self.__impuestoSellos

    # setter del atributo impuestoSellos
    @impuestoSellos.setter
    def impuestoSellos(self, valor):
        self.__impuestoSellos = valor

    # getter del atributo impuestoSellosPartes
    @property
    def impuestoSellosPartes(self):
        return self.__impuestoSellosPartes

    # setter del atributo impuestoSellosPartes
    @impuestoSellosPartes.setter
    def impuestoSellosPartes(self, valor):
        self.__impuestoSellosPartes = valor

    # getter del atributo impuestoSellosPartesTipoTramite
    @property
    def impuestoSellosPartesTipoTramite(self):
        return self.__impuestoSellosPartesTipoTramite

    # setter del atributo impuestoSellosPartesTipoTramite
    @impuestoSellosPartesTipoTramite.setter
    def impuestoSellosPartesTipoTramite(self, valor):
        self.__impuestoSellosPartesTipoTramite = valor

    # getter del atributo impuestoAutomotor
    @property
    def impuestoAutomotor(self):
        return self.__impuestoAutomotor

    # setter del atributo impuestoAutomotor
    @impuestoAutomotor.setter
    def impuestoAutomotor(self, valor):
        self.__impuestoAutomotor = valor

    # getter del atributo informacionVehiculo
    @property
    def informacionVehiculo(self):
        return self.__informacionVehiculo

    # setter del atributo informacionVehiculo
    @informacionVehiculo.setter
    def informacionVehiculo(self, valor):
        self.__informacionVehiculo = valor

    # getter del atributo informacionVehiculoTitular
    @property
    def informacionVehiculoTitular(self):
        return self.__informacionVehiculoTitular

    # setter del atributo informacionVehiculoTitular
    @informacionVehiculoTitular.setter
    def informacionVehiculoTitular(self, valor):
        self.__informacionVehiculoTitular = valor

    # getter del atributo tmpInformacionVehiculo
    @property
    def tmpInformacionVehiculo(self):
        return self.__tmpInformacionVehiculo

    # setter del atributo tmpInformacionVehiculo
    @tmpInformacionVehiculo.setter
    def tmpInformacionVehiculo(self, valor):
        self.__tmpInformacionVehiculo = valor

    # getter del atributo tmpInformacionVehiculoTitular
    @property
    def tmpInformacionVehiculoTitular(self):
        return self.__tmpInformacionVehiculoTitular

    # setter del atributo tmpInformacionVehiculoTitular
    @tmpInformacionVehiculoTitular.setter
    def tmpInformacionVehiculoTitular(self, valor):
        self.__tmpInformacionVehiculoTitular = valor

    # getter del atributo cambioTitularidad
    @property
    def cambioTitularidad(self):
        return self.__cambioTitularidad

    # setter del atributo cambioTitularidad
    @cambioTitularidad.setter
    def cambioTitularidad(self, valor):
        self.__cambioTitularidad = valor

    # getter del atributo cambioTitularidadTitular
    @property
    def cambioTitularidadTitular(self):
        return self.__cambioTitularidadTitular

    # setter del atributo cambioTitularidadTitular
    @cambioTitularidadTitular.setter
    def cambioTitularidadTitular(self, valor):
        self.__cambioTitularidadTitular = valor

    # getter del atributo informacionRadicacion
    @property
    def informacionRadicacion(self):
        return self.__informacionRadicacion

    # getter del atributo informacionRadicacion
    @informacionRadicacion.setter
    def informacionRadicacion(self, valor):
        self.__informacionRadicacion = valor

    # getter del atributo anulacionTramitesSellos
    @property
    def anulacionTramitesSellos(self):
        return self.__anulacionTramitesSellos

    # setter del atributo anulacionTramitesSellos
    @anulacionTramitesSellos.setter
    def anulacionTramitesSellos(self, valor):
        self.__anulacionTramitesSellos = valor

    # getter del atributo anulacionTramitesSellosDetalle
    @property
    def anulacionTramitesSellosDetalle(self):
        return self.__anulacionTramitesSellosDetalle

    # setter del atributo anulacionTramitesSellosDetalle
    @anulacionTramitesSellosDetalle.setter
    def anulacionTramitesSellosDetalle(self, valor):
        self.__anulacionTramitesSellosDetalle = valor

    # getter del atributo tramitesGenerales
    @property
    def tramitesGenerales(self):
        return self.__tramitesGenerales

    # setter del atributo tramitesGenerales
    @tramitesGenerales.setter
    def tramitesGenerales(self, valor):
        self.__tramitesGenerales = valor

    # getter del atributo tramitesGeneralesTitular
    @property
    def tramitesGeneralesTitular(self):
        return self.__tramitesGeneralesTitular

    # getter del atributo tramitesGeneralesTitular
    @tramitesGeneralesTitular.setter
    def tramitesGeneralesTitular(self, valor):
        self.__tramitesGeneralesTitular = valor

    # getter del atributo pie
    @property
    def pie(self):
        return self.__pie

    # getter del atributo pie
    @pie.setter
    def pie(self, valor):
        self.__pie = valor

    # getter del atributo apiAumoso
    @property
    def apiAumoso(self):
        return self.__apiAumoso

    # getter del atributo apiAumoso
    @apiAumoso.setter
    def apiAumoso(self, valor):
        self.__apiAumoso = valor

    # getter del atributo apiToken
    @property
    def apiToken(self):
        return self.__apiToken

    # setter del atributo apiToken
    @apiToken.setter
    def apiToken(self, valor):
        self.__apiToken = valor

    # getter del atributo apiTokenUser
    @property
    def apiTokenUser(self):
        return self.__apiTokenUser
    
    # setter del atributo apiTokenUser
    @apiTokenUser.setter
    def apiTokenUser(self, valor):
        self.__apiTokenUser = valor

    # getter del atributo apiTokenUserRef
    @property
    def apiTokenUserRef(self):
        return self.__apiTokenUserRef

    # setter del atributo apiTokenUserRef
    @apiTokenUserRef.setter
    def apiTokenUserRef(self, valor):
        self.__apiTokenUserRef = valor

    # getter del atributo apiRegistros
    @property
    def apiRegistros(self):
        return self.__apiRegistros

    # setter del atributo apiRegistros
    @apiRegistros.setter
    def apiRegistros(self, valor):
        self.__apiRegistros = valor

    # getter del atributo apiEstados
    @property
    def apiEstados(self):
        return self.__apiEstados

    # setter del atributo apiEstados
    @apiEstados.setter
    def apiEstados(self, valor):
        self.__apiEstados = valor

    # getter del atributo apiTareas
    @property
    def apiTareas(self):
        return self.__apiTareas

    # setter del atributo apiTareas
    @apiTareas.setter
    def apiTareas(self, valor):
        self.__apiTareas = valor

    # getter del atributo apiEstadosTareas
    @property
    def apiEstadosTareas(self):
        return self.__apiEstadosTareas

    # setter del atributo apiEstadosTareas
    @apiEstadosTareas.setter
    def apiEstadosTareas(self, valor):
        self.__apiEstadosTareas = valor

    # getter del atributo relArbaSucerpMarca
    @property
    def relArbaSucerpMarca(self):
        return self.__relArbaSucerpMarca

    # setter del atributo relArbaSucerpMarca
    @relArbaSucerpMarca.setter
    def relArbaSucerpMarca(self, valor):
        self.__relArbaSucerpMarca = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo procesoImportacionExportacion
    @property
    def procesoImportacionExportacion(self):
        return self.__procesoImportacionExportacion

    # setter del atributo procesoImportacionExportacion
    @procesoImportacionExportacion.setter
    def procesoImportacionExportacion(self, valor):
        self.__procesoImportacionExportacion = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo apiLog
    @property
    def apiLog(self):
        return self.__apiLog

    # setter del atributo apiLog
    @apiLog.setter
    def apiLog(self, valor):
        self.__apiLog = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla procesoImportacionExportacion_Dal
    @property
    def procesoImportacionExportacion_Dal(self):

        try:

            # si el atributo no esta asignado        
            if self.procesoImportacionExportacion is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.procesoImportacionExportacion = self.__buildTable(
                    self.formatosSucerp.tablaProcesoImportacionExportacion())

            # retornamos el objeto tabla
            return self.procesoImportacionExportacion

        except Exception as inst:
            print(f'Error - procesoImportacionExportacion_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoMovimiento_Dal
    @property
    def tipoMovimiento_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoMovimiento is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp
                self.tipoMovimiento = self.__buildTable(
                    self.formatosSucerp.tablaTipoMovimiento())

            # retornamos el objeto tabla
            return self.tipoMovimiento

        except Exception as inst:
            print(f'Error - tipoMovimiento_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ENCABEZADO
    #     FOR SYSTEM NAME ------------------------
    #@property
    #def encabezado_Dal(self):
    #    if self.encabezado is None:
    #        migrate = False
    #        #self.encabezado = self.__buildTable(
    # self.formatosSucerp.tablaEncabezado(migrate=migrate))
    #    return self.encabezado

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoRegistro_Dal
    @property
    def tipoRegistro_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoRegistro is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.tipoRegistro = self.__buildTable(
                    self.formatosSucerp.tablaTipoRegistro())

            # retornamos el objeto tabla
            return self.tipoRegistro

        except Exception as inst:
            print(f'Error - tipoRegistro_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoSubRegistro_Dal
    @property
    def tipoSubRegistro_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoSubRegistro is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.tipoSubRegistro = self.__buildTable(
                    self.formatosSucerp.tablaTipoSubRegistro())

            # retornamos el objeto tabla
            return self.tipoSubRegistro
        
        except Exception as inst:
            print(f'Error - tipoSubRegistro_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla procesoImportacionExportacion_Dal
    @property
    def tipoCuerpo_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoCuerpo is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.tipoCuerpo = self.__buildTable(
                    self.formatosSucerp.tablaTipoCuerpo())

            # retornamos el objeto tabla
            return self.tipoCuerpo

        except Exception as inst:
            print(f'Error - tipoCuerpo_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoCuerpo_Dal        
    @property
    def tipoTitular_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoTitular is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp
                self.tipoTitular = self.__buildTable(
                    self.formatosSucerp.tablaTipoTitular())

            # retornamos el objeto tabla
            return self.tipoTitular
    
        except Exception as inst:
            print(f'Error - tipoTitular_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoOrigen_Dal    
    @property
    def tipoOrigen_Dal(self):

        try:

            # si el atributo no fue asignado    
            if self.tipoOrigen is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.tipoOrigen = self.__buildTable(
                    self.formatosSucerp.tablaTipoOrigen())

            # retorno del objeto tabla
            return self.tipoOrigen

        except Exception as inst:
            print(f'Error - tipoOrigen_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoCuota_Dal
    @property
    def tipoCuota_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoCuota is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp
                self.tipoCuota = self.__buildTable(
                    self.formatosSucerp.tablaTipoCuota())

            # retornamos el objeto tabla
            return self.tipoCuota

        except Exception as inst:
            print(f'Error - tipoCuota_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoPago_Dal
    @property
    def tipoPago_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoPago is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp            
                self.tipoPago = self.__buildTable(
                    self.formatosSucerp.tablaTipoPago())

            # retornamos el objeto tabla
            return self.tipoPago

        except Exception as inst:
            print(f'Error - tipoPago_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoMoneda_Dal
    @property
    def tipoMoneda_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoMoneda is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                        
                self.tipoMoneda = self.__buildTable(
                    self.formatosSucerp.tablaTipoMoneda())

            # retornamos el objeto tabla
            return self.tipoMoneda
        
        except Exception as inst:
            print(f'Error - tipoMoneda_Dal {e}')
            return inst                        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla tipoDocumento_Dal
    @property
    def tipoDocumento_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.tipoDocumento is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                    
                self.tipoDocumento = self.__buildTable(
                    self.formatosSucerp.tablaTipoDocumento())

            # retornamos el objeto tabla
            return self.tipoDocumento

        except Exception as inst:
            print(f'Error - tipoDocumento_Dal {e}')
            return inst                

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla provincias_Dal
    @property
    def provincias_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.provincias is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                
                self.provincias = self.__buildTable(
                    self.formatosSucerp.tablaProvincias())

            # retornamos el objeto tabla
            return self.provincias

        except Exception as inst:
            print(f'Error - provincias_Dal {e}')
            return inst                

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla estado_Dal
    @property
    def estado_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.estado is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                
                self.estado = self.__buildTable(self.formatosSucerp.tablaEstado())

            # retornamos el objeto tabla
            return self.estado
        
        except Exception as inst:
            print(f'Error - estado_Dal {e}')
            return inst                

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla registroEncabezado_Dal
    @property
    def registroEncabezado_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.registroEncabezado is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo
                    self.tipoRegistro = self.tipoRegistro_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.registroEncabezado = self.__buildTable(
                    self.formatosSucerp.tablaEncabezado())

                # asignamos la lista de Tablas de referencias
                self.registroEncabezado._referenced_by_list = [self.tipoRegistro]

            # retornamos el objeto tabla
            return self.registroEncabezado
        
        except Exception as inst:
            print(f'Error - registroEncabezado_Dal {e}')
            return inst        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla relArbaSucerpMarca_Dal
    @property
    def relArbaSucerpMarca_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.relArbaSucepMarca is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                                        
                self.relArbaSucepMarca = self.__buildTable(
                    self.formatosSucerp.tablaRelArbaSucerpMarca())

            # retornamos el objeto tabla
            return self.relArbaSucepMarca

        except Exception as inst:
            print(f'Error - relArbaSucerpMarca_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla altaImpositiva_Dal
    @property
    def altaImpositiva_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.altaImpositiva is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo                    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoOrigen is None:

                    # asignamos el atributo                    
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoDocumento is None:

                    # asignamos el atributo                    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a tipos de registros no esta asignado
                if self.provincias is None:

                    # asignamos el atributo                    
                    self.provincias = self.provincias_Dal

                # Referencias a tipos de registros no esta asignado
                if self.altaImpositivaTitular is None:

                    # asignamos el atributo                    
                    self.altaImpositivaTitular = self.altaImpositivaTitular_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.altaImpositiva = self.__buildTable(
                    self.formatosSucerp.tablaAltaImpositiva())

                # asignamos la list de Tablas de referencias
                self.altaImpositiva._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro,
                    self.tipoOrigen, self.tipoDocumento, self.provincias,
                    self.altaImpositivaTitular
                ]

            # retornamos el objeto tabla
            return self.altaImpositiva

        except Exception as inst:
            print(f'Error - altaImpositiva_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla altaImpositivaTitular_Dal
    @property
    def altaImpositivaTitular_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.altaImpositivaTitular is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoCuerpo is None:

                    # asignamos el atributo                    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo                    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoDocumento is None:

                    # asignamos el atributo                        
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a tipos de registros no esta asignado
                if self.provincias is None:

                    # asignamos el atributo                        
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.altaImpositivaTitular = self.__buildTable(
                    self.formatosSucerp.tablaAltaImpositivaTitular())

                # asignamos la list de Tablas de referencias
                self.altaImpositivaTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]

            # retornamos el objeto tabla
            return self.altaImpositivaTitular

        except Exception as inst:
            print(f'Error - altaImpositivaTitular_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla anulacionTramitesSellos_Dal
    @property
    def anulacionTramitesSellos_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.anulacionTramitesSellos is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoOrigen is None:

                    # asignamos el atributo
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoPago is None:

                    # asignamos el atributo
                    self.tipoPago = self.tipoPago_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoMoneda is None:

                    # asignamos el atributo
                    self.tipoMoneda = self.tipoMoneda_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.anulacionTramitesSellos = self.__buildTable(
                    self.formatosSucerp.tablaAnulacionTramitesSellos())

                # asignamos la list de Tablas de referencias
                self.anulacionTramitesSellos._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoPago, self.tipoMoneda
                ]

            # retornamos el objeto tabla
            return self.anulacionTramitesSellos
        
        except Exception as inst:
            print(f'Error - anulacionTramitesSellos_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla anulacionTramitesSellosDetalle_Dal
    @property
    def anulacionTramitesSellosDetalle_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.anulacionTramitesSellosDetalle is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo                    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo                    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoCuota is None:

                    # asignamos el atributo                    
                    self.tipoCuota = self.tipoCuota_Dal

                # Referencias a tipos de registros no esta asignado
                if self.anulacionTramitesSellos is None:

                    # asignamos el atributo                    
                    self.anulacionTramitesSellos = self.anulacionTramitesSellos_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.anulacionTramitesSellosDetalle = self.__buildTable(
                    self.formatosSucerp.tablaAnulacionTramitesSellosDetalle())

                # asignamos la list de Tablas de referencias
                self.anulacionTramitesSellosDetalle._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoCuota, self.anulacionTramitesSellos
                ]

            # retornamos el objeto tabla
            return self.anulacionTramitesSellosDetalle

        except Exception as inst:
            print(f'Error - anulacionTramitesSellosDetalle_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiEstados_Dal
    @property
    def apiEstados_Dal(self):

        try:

            # si el atributo no esta asignado        
            if self.apiEstados is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.apiEstados = self.__buildTable(
                    self.formatosSucerp.tablaApiEstados())

            # retornamos el objeto tabla
            return self.apiEstados

        except Exception as inst:
            print(f'Error - apiEstados_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiTareas_Dal
    @property
    def apiTareas_Dal(self):

        try:

            # si el atributo no esta asignado        
            if self.apiTareas is None:
            
                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp                                                            
                self.apiTareas = self.__buildTable(
                    self.formatosSucerp.tablaApiTareas())
                
            # retornamos el objeto tabla
            return self.apiTareas
        
        except Exception as inst:
            print(f'Error - apiTareas_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiEstadosTareas_Dal
    @property
    def apiEstadosTareas_Dal(self):
        try:

            # si el atributo no esta asignado
            if self.apiEstadosTareas is None:

                # Referencias a tipos de registros no esta asignado
                if self.apiEstados is None:

                    # asignamos el atributo                    
                    self.apiEstados = self.apiEstados_Dal

                # Referencias a tipos de registros no esta asignado
                if self.apiTareas is None:

                    # asignamos el atributo                    
                    self.apiTareas = self.apiTareas_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.apiEstadosTareas = self.__buildTable(
                    self.formatosSucerp.tablaApiEstadosTareas())

                # asignamos la list de Tablas de referencias
                self.apiEstadosTareas._referenced_by_list = [
                    self.apiEstados, self.apiTareas
                ]

            # retornamos el objeto tabla
            return self.apiEstadosTareas
        
        except Exception as inst:
            print(f'Error - apiEstadosTareas_Dal {e}')
            return inst    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiRegistros_Dal
    @property
    def apiRegistros_Dal(self):

        try:

            # si el atributo no esta asignado
            if self.apiRegistros is None:

                # Referencias a tipos de registros no esta asignado
                if self.apiEstadosTareas is None:

                    # asignamos el atributo                                        
                    self.apiEstadosTareas = self.apiEstadosTareas_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.apiRegistros = self.__buildTable(
                    self.formatosSucerp.tablaApiRegistros())

                # asignamos la lista de Tablas de referencias
                self.apiRegistros._referenced_by_list = [self.apiEstadosTareas]

            # retornamos el objeto tabla
            return self.apiRegistros
        
        except Exception as inst:
           print(f'Error - apiRegistros_Dal {e}')
           return inst        

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiTokenUser_Dal
    @property
    def apiTokenUser_Dal(self):

        try:

            # si el atributo no esta asignado            
            if self.apiTokenUser is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoDocumento is None:

                    # asignamos el atributo                                        
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a tipos de registros no esta asignado
                if self.apiRegistros is None:

                    # asignamos el atributo                                            
                    self.apiRegistros = self.apiRegistros_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.apiTokenUser = self.__buildTable(
                    self.formatosSucerp.tablaApiTokenUser())

                # asignamos la lista de Tablas de referencias
                self.apiTokenUser._referenced_by_list = [self.tipoDocumento, self.apiRegistros]

            # retornamos el objeto tabla
            return self.apiTokenUser

        except Exception as inst:
           print(f'Error - apiTokenUser_Dal {e}')
           return inst            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiLog_Dal
    @property
    def apiLog_Dal(self):

        try:

            # si el atributo no esta asignado            
            if self.apiLog is None:

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.apiLog = self.__buildTable(
                    self.formatosSucerp.tablaApiLog())

            # retornamos el objeto tabla
            return self.apiLog

        except Exception as inst:
           print(f'Error - apiLog_Dal {e}')
           return inst            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tabla apiToken_Dal
    @property
    def apiToken_Dal(self):

        try:

            # si el atributo no esta asignado            
            if self.apiToken is None:

                # Referencias a tipos de registros no esta asignado
                if self.apiTokenUser is None:

                    # asignamos el atributo
                    self.apiTokenUser = self.apiTokenUser_Dal

                # Referencias a tipos de registros no esta asignado
                if self.__apiRegistros is None:

                    # asignamos el atributo                                                                    
                    self.__apiRegistros = self.apiRegistros_Dal

                # Referencias a tipos de registros no esta asignado
                if self.apiEstadosTareas is None:

                    # asignamos el atributo
                    self.apiEstadosTareas = self.apiEstadosTareas_Dal

                if self.apiToken is None:

                    # asignamos la construccion del objeto tabla 
                    # de la instancia clase AtributosSucerp      
                    self.apiToken = self.__buildTable(
                        self.formatosSucerp.tablaApiToken())

                # asignamos la lista de Tablas de referencias
                self.apiToken._referenced_by_list = [
                    self.apiTokenUser, self.apiRegistros, 
                    self.apiEstadosTareas
                ]

            # retornamos el objeto tabla
            return self.apiToken
        
        
        except Exception as inst:
           print(f'Error - apiToken_Dal {e}')
           return inst                    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto bajaImpositiva_Dal
    @property
    def bajaImpositiva_Dal(self):

        try:

            # si el atributo no esta asignado                
            if self.bajaImpositiva is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoOrigen is None:

                    # asignamos el atributo
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Referencias a tipos de registros no esta asignado
                if self.bajaImpositivaTitular is None:

                    # asignamos el atributo
                    self.bajaImpositivaTitular = self.bajaImpositivaTitular_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.bajaImpositiva = self.__buildTable(
                    self.formatosSucerp.tablaBajaImpositiva())

                # asignamos la lista de Tablas de referencias
                self.bajaImpositiva._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.bajaImpositivaTitular
                ]

            # retornamos el objeto tabla
            return self.bajaImpositiva
        
        except Exception as inst:
           print(f'Error - bajaImpositiva_Dal {e}')
           return inst                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto bajaImpositivaTitular_Dal
    @property
    def bajaImpositivaTitular_Dal(self):

        try:

            # si el atributo no esta asignado                
            if self.bajaImpositivaTitular is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoCuerpo is None:

                    # asignamos el atributo                    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoDocumento is None:

                    # asignamos el atributo
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a tipos de registros no esta asignado
                if self.provincias is None:

                    # asignamos el atributo
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.bajaImpositivaTitular = self.__buildTable(
                    self.formatosSucerp.tablaBajaImpositivaTitular())

                # asignamos la lista de Tablas de referencias
                self.bajaImpositivaTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]

            # retornamos el objeto tabla
            return self.bajaImpositivaTitular
        
        except Exception as inst:
           print(f'Error - bajaImpositivaTitular_Dal {e}')
           return inst                                    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto cambioTitularidad_Dal
    @property
    def cambioTitularidad_Dal(self):

        try:

            # si el atributo no esta asignado                
            if self.cambioTitularidad is None:

                # Referencias a tipos de registros no esta asignado
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoSubRegistro is None:

                    # asignamos el atributo
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoCuerpo is None:

                    # asignamos el atributo
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de registros no esta asignado
                if self.tipoDocumento is None:

                    # asignamos el atributo
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a tipos de registros no esta asignado
                if self.provincias is None:

                    # asignamos el atributo
                    self.provincias = self.provincias_Dal

                # Referencias a tipos de registros no esta asignado
                if self.cambioTitularidadTitular is None:

                    # asignamos el atributo
                    self.cambioTitularidadTitular = self.cambioTitularidadTitular_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.cambioTitularidad = self.__buildTable(
                    self.formatosSucerp.tablaCambioTitularidad())

                # asignamos la lista de Tablas de referencias
                self.cambioTitularidad._referenced_by_list = [
                    self.tipoRegistro, self.tipoCuerpo, 
                    self.tipoSubRegistro, self.tipoDocumento, 
                    self.provincias,
                    self.cambioTitularidadTitular
                ]

            # retornamos el objeto tabla
            return self.cambioTitularidad
        
        except Exception as inst:
           print(f'Error - cambioTitularidad_Dal {e}')
           return inst                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto cambioTitularidadTitular_Dal
    @property
    def cambioTitularidadTitular_Dal(self):

        try:

            # si el atributo no esta asignado                
            if self.cambioTitularidadTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Titular
                if self.tipoTitular is None:

                    # asignamos el atributo
                    self.tipoTitular = self.tipoTitular_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:

                    # asignamos el atributo
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:

                    # asignamos el atributo
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.cambioTitularidadTitular = self.__buildTable(
                    self.formatosSucerp.tablaCambioTitularidadTitular())

                # asignamos la lista de Tablas de referencias
                self.cambioTitularidadTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoTitular, self.tipoDocumento, 
                    self.provincias
                ]

            # retornamos el objeto tabla
            return self.cambioTitularidadTitular
    
        except Exception as inst:
           print(f'Error - cambioTitularidadTitular_Dal {e}')
           return inst                                                

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto impuestoAutomotor_Dal
    @property
    def impuestoAutomotor_Dal(self):

        try:

            # si el atributo no esta asignado                
            if self.impuestoAutomotor is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Movimeinto
                if self.tipoMovimiento is None:

                    # asignamos el atributo
                    self.tipoMovimiento = self.tipoMovimiento_Dal

                # Tabla tipo de Registro
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de Pago
                if self.tipoPago is None:

                    # asignamos el atributo
                    self.tipoPago = self.tipoPago_Dal

                # Referencias a tipos de Monedas
                if self.tipoMoneda is None:

                    # asignamos el atributo
                    self.tipoMoneda = self.tipoMoneda_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.impuestoAutomotor = self.__buildTable(
                    self.formatosSucerp.tablaImpuestoAutomotor())

                # asignamos la lista de Tablas de referencias
                self.impuestoAutomotor._referenced_by_list = [
                    self.tipoCuerpo, self.tipoMovimiento, 
                    self.tipoRegistro, self.tipoPago, self.tipoMoneda
                ]

            # retornamos el objeto tabla
            return self.impuestoAutomotor
    
        except Exception as inst:
           print(f'Error - impuestoAutomotor_Dal {e}')
           return inst                                                    

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto impuestoSellos_Dal
    @property
    def impuestoSellos_Dal(self):
            
        try:            

            # si el atributo no esta asignado                
            if self.impuestoSellos is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:

                    # asignamos el atributo    
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla tipo de Pago
                if self.tipoPago is None:

                    # asignamos el atributo    
                    self.tipoPago = self.tipoPago_Dal

                # Tabla tipo de Moneda
                if self.tipoMoneda is None:

                    # asignamos el atributo    
                    self.tipoMoneda = self.tipoMoneda_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.impuestoSellos = self.__buildTable(
                    self.formatosSucerp.tablaImpuestosSellos())

                # asignamos la lista de Tablas de referencias
                self.impuestoSellos._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoPago, self.tipoMoneda
                ]

            # retornamos el objeto tabla
            return self.impuestoSellos
        
        except Exception as inst:
           print(f'Error - impuestoSellos_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto impuestoSellosPartes_Dal
    @property
    def impuestoSellosPartes_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.impuestoSellosPartes is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo        
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:

                    # asignamos el atributo    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de Provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.impuestoSellosPartes = self.__buildTable(
                    self.formatosSucerp.tablaImpuestosSellosPartes())

                # asignamos la lista de Tablas de referencias
                self.impuestoSellosPartes._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias
                ]

            # retornamos el objeto tabla
            return self.impuestoSellosPartes

        except Exception as inst:
           print(f'Error - impuestoSellosPartes_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto impuestoSellosPartesTipoTramite_Dal
    @property
    def impuestoSellosPartesTipoTramite_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.impuestoSellosPartesTipoTramite is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.impuestoSellosPartesTipoTramite = self.__buildTable(
                    self.formatosSucerp.tablaImpuestosSellosPartesTipoTramite())

                # asignamos la lista de Tablas de referencias
                self.impuestoSellosPartesTipoTramite._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro
                ]

            # retornamos el objeto tabla
            return self.impuestoSellosPartesTipoTramite

        except Exception as inst:
           print(f'Error - impuestoSellosPartesTipoTramite_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto informacionVehiculo_Dal
    @property
    def informacionVehiculo_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.informacionVehiculo is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:

                    # asignamos el atributo    
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.informacionVehiculo = self.__buildTable(
                    self.formatosSucerp.tablaInformacionVehiculo())

                # asignamos la lista de Tablas de referencias
                self.informacionVehiculo._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.provincias
                ]


            # retornamos el objeto tabla
            return self.informacionVehiculo

        except Exception as inst:
           print(f'Error - informacionVehiculo_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tmpInformacionVehiculo_Dal
    @property
    def tmpInformacionVehiculo_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.tmpInformacionVehiculo is None:

                # Tabla tipo de Registro
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:

                    # asignamos el atributo    
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.tmpInformacionVehiculo = self.__buildTable(
                    self.formatosSucerp.tablaTmpInformacionVehiculo())


            # retornamos el objeto tabla
            return self.tmpInformacionVehiculo

        except Exception as inst:
           print(f'Error - tmpInformacionVehiculo_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto informacionVehiculoTitular_Dal
    @property
    def informacionVehiculoTitular_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.informacionVehiculoTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:

                    # asignamos el atributo    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # Tabla de informacion de Vehiculo
                if self.informacionVehiculo is None:

                    # asignamos el atributo    
                    self.informacionVehiculo = self.informacionVehiculo_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.informacionVehiculoTitular = self.__buildTable(
                    self.formatosSucerp.tablaInformacionVehiculoTitular())

                # asignamos la lista de Tablas de referencias
                self.informacionVehiculoTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, 
                    self.tipoDocumento, self.provincias,
                    self.informacionVehiculo
                ]

            # retornamos el objeto tabla
            return self.informacionVehiculoTitular


        except Exception as inst:
           print(f'Error - informacionVehiculoTitular_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tmpInformacionVehiculoTitular_Dal
    @property
    def tmpInformacionVehiculoTitular_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.tmpInformacionVehiculoTitular is None:

                # Tabla tipo de Cuerpo
                if self.tipoCuerpo is None:

                    # asignamos el atributo    
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Tabla tipo de Sub Registros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:

                    # asignamos el atributo    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # Tabla de informacion de Vehiculo
                if self.tmpInformacionVehiculo is None:

                    # asignamos el atributo    
                    self.tmpInformacionVehiculo = self.tmpInformacionVehiculo_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.tmpInformacionVehiculoTitular = self.__buildTable(
                    self.formatosSucerp.tablaTmpInformacionVehiculoTitular())

            # retornamos el objeto tabla
            return self.tmpInformacionVehiculoTitular

        except Exception as inst:
           print(f'Error - tmpInformacionVehiculoTitular_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto informacionRadicacion_Dal
    @property
    def informacionRadicacion_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.informacionRadicacion is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de Esatdos
                if self.estado is None:

                    # asignamos el atributo    
                    self.estado = self.estado_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.informacionRadicacion = self.__buildTable(
                    self.formatosSucerp.tablaInformacionRadicacion())

                # Tablas de referencias
                self.informacionRadicacion._referenced_by_list = [
                    self.tipoRegistro, self.estado
                ]

            # retornamos el objeto tabla
            return self.informacionRadicacion

        except Exception as inst:
           print(f'Error - informacionRadicacion_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto anulacionTramitesSellosDetalle_Dal
    @property
    def anulacionTramitesSellosDetalle_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.anulacionTramitesSellosDetalle is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de SubRegistros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Cuota
                if self.tipoCuota is None:

                    # asignamos el atributo    
                    self.tipoCuota = self.tipoCuota_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.anulacionTramitesSellosDetalle = self.__buildTable(
                    self.formatosSucerp.tablaAnulacionTramitesSellosDetalle())

                # Tablas de referencias
                self.anulacionTramitesSellosDetalle._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, self.tipoCuota
                ]

            # retornamos el objeto tabla
            return self.anulacionTramitesSellosDetalle

        except Exception as inst:
           print(f'Error - anulacionTramitesSellosDetalle_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tramitesGenerales_Dal
    @property
    def tramitesGenerales_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.tramitesGenerales is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de SubRegistros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Origen
                if self.tipoOrigen is None:

                    # asignamos el atributo    
                    self.tipoOrigen = self.tipoOrigen_Dal

                # Tabla tipo de Documentos
                if self.tipoDocumento is None:

                    # asignamos el atributo    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla tramitesgeneralestitular
                if self.tramitesGeneralesTitular is None:

                    # asignamos el atributo    
                    self.tramitesGeneralesTitular = self.tramitesGeneralesTitular_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.tramitesGenerales = self.__buildTable(
                    self.formatosSucerp.tablaTramitesGenerales())

                # asignamos la lista de Tablas de referencias
                self.tramitesGenerales._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoOrigen, self.tipoDocumento,
                    self.tramitesGeneralesTitular
                ]

            # retornamos el objeto tabla
            return self.tramitesGenerales

        except Exception as inst:
           print(f'Error - tramitesGenerales_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto tramitesGeneralesTitular_Dal
    @property
    def tramitesGeneralesTitular_Dal(self):

        try:            

            # si el atributo no esta asignado                
            if self.tramitesGeneralesTitular is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Tabla tipo de SubRegistros
                if self.tipoSubRegistro is None:

                    # asignamos el atributo    
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Tabla tipo de Titular
                if self.tipoTitular is None:

                    # asignamos el atributo    
                    self.tipoTitular = self.tipoTitular_Dal

                # Tabla tipo de Documento
                if self.tipoDocumento is None:

                    # asignamos el atributo    
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Tabla de provincias
                if self.provincias is None:

                    # asignamos el atributo    
                    self.provincias = self.provincias_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.tramitesGeneralesTitular = self.__buildTable(
                    self.formatosSucerp.tablaTramitesGeneralesTitulares())

                # asignacion de la lista de Tablas de referencias
                self.tramitesGeneralesTitular._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, 
                    self.tipoTitular, self.tipoDocumento,
                    self.provincias
                ]

            # retornamos el objeto tabla
            return self.tramitesGeneralesTitular

        except Exception as inst:
           print(f'Error - tramitesGeneralesTitular_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto pie_Dal
    @property
    def pie_Dal(self):

        try:         

            # si el atributo no esta asignado                
            if self.pie is None:

                # Tabla tipo de Registros
                if self.tipoRegistro is None:

                    # asignamos el atributo    
                    self.tipoRegistro = self.tipoRegistro_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.pie = self.__buildTable(self.formatosSucerp.tablaPie())

                # Tablas de referencias
                self.pie._referenced_by_list = [
                    self.tipoRegistro
                ]

            # retornamos el objeto tabla
            return self.pie

        except Exception as inst:
           print(f'Error - pie_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del objeto apiAumoso_Dal
    @property
    def apiAumoso_Dal(self):

        try:         

            # si el atributo no esta asignado                
            if self.apiAumoso is None:

                # Tabla api Token
                if self.apiToken is None:

                    # asignamos el atributo    
                    self.apiToken = self.apiToken_Dal

                # asignamos la construccion del objeto tabla 
                # de la instancia clase AtributosSucerp      
                self.apiAumoso = self.__buildTable(
                    self.formatosSucerp.tablaApiAumoso())

                # Tablas de referencias
                self.apiToken._referenced_by_list = [ self.apiToken ]

            # retornamos el objeto tabla
            return self.apiAumoso

        except Exception as inst:
           print(f'Error - apiAumoso_Dal {e}')
           return inst                                                            

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    @property
    def msgNivelGravedad_Dal(self):
        if self.__msgNivelGravedad is None:
            try:
                self.__msgNivelGravedad = self.db.define_table(
                    'MSGNIVELGRAVEDAD',
                    Field('NIVELGRAVEDADID', type='id', label='Id'),
                    Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50, required=True, label='Descripcion'),
                    Field('MSGNIVELGRAVEDADALERTA', type='string', length=50, required=True, label='Ayuda Mensaje'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__msgNivelGravedad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    @property
    def mensajeError_Dal(self):
        if self.__mensajesError is None:
            try:
                self.__mensajesError = self.db.define_table(
                    'MENSAJESERROR',
                    Field('MSGCODE', type='string', length=7, required=True, label='Mensaje Codigo'),
                    Field('MSGDESCRIPCION', type='string', length=150, required=True, label='Descripcion'),
                    Field('MSGHELP', type='string', length=1024, required=True, label='Ayuda Mensaje'),
                    Field('NIVELGRAVEDADID', 'reference MSGNIVELGRAVEDAD', label='Id', ondelete='CASCADE'),
                    primarykey=['MSGCODE'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesError

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    @property
    def mensajesErrorMsgdDinamicos_Dal(self):
        if self.__mensajesErrorMsgdDinamicos is None:
            try:
                self.__mensajesErrorMsgdDinamicos = self.db.define_table(
                    'MENSAJESERRORMSGDINAMICOS',
                    Field('MSGCODE', type='integer', required=True, label='Codigo del Mensaje'),
                    Field('MSGDINAMICOID', type='integer', required=True, label='Mensaje Dinamico Id'),
                    Field('MSGDINAMICOLEN', type='integer', required=True, label='Ayuda Mensaje'),
                    primarykey=['MSGCODE', 'MSGDINAMICOID'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesErrorMsgdDinamicos

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.IMPRESIONPDF
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def impresionPdf_Dal(self):
        if self.__impresionPdf is None:
            try:
                self.__impresionPdf = self.db.define_table(
                    'IMPRESIONPDF',
                    Field('IMPRESIONID', type='id', label='Inmpresion Id'),
                    Field('IMPRESIONPRMUNO', type='string', length=512, required=True, label='Parametro Uno'),
                    Field('IMPRESIONPRMDOS', type='string', length=512, required=True, label='Parametro Dos'),
                    Field('IMPRESIONUSUARIO', type='string', length=10, required=True, label='Usuario'),
                    Field('IMPRESIONFECHA', type='datetime', required=True, label='Fecha'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__impresionPdf

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # constructor de objeto tabla ya definidas
    def __buildTable(self, parm):

        """
        parm = Parámetros para la construcción de la tabla
        retorno un objeto tabla
        """

        try:

            # create  table
            valor = self.db.define_table(parm['name'], *parm['fields'], **parm['arg'])

            # if the environment allows to generate LABEL ON
            if parm['arg']['migrate']:

                # determina si el ambiente esta dentro los ambientes que soporta 
                # la clausula LABEL_ON    
                if ConfigurarAplicacion.ENV_GX in ConfigurarAplicacion.ENV_LABEL_ON:

                    texto = ''

                    # we iterate through the fields of the table record
                    for x in range(0, len(valor._fields)):

                        # we build the text variable
                        texto += f'\"{valor._fields[x].lower()}\" text is \'{valor.__getattribute__(valor._fields[x]).comment}\''

                        if x != (len(valor._fields) - 1):
                            texto += ' ,'

                    # we build the sentencia variable
                    sentencia = f'LABEL ON COLUMN {valor._dalname} ({texto})'

                    # execute the sql statement para colocar el LABEL ON COLUMN
                    self.db.executesql(sentencia)


        except Exception as inst:
            print(inst)
            return inst

        # aplicacion  de los campos
        self.db.commit()

        # retorno el objeto tabla generado
        return valor

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# clase que maneja la definicion de la tablas del esquema Matanza
class MatanzaAbstractDb():
    """
     EL OBJETIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE CADA TABLA QUE ESTAMN EL MOTOR ISERIES O MYSQL \n
     CUANDO TRABAJAMOS SIN CONEXION A LAS TABLAS DE ISERIES SE TRABAJA CON MYSQL \n

    """

    # Constructor
    def __init__(self, db):

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas de Matanza
        self.__tmAut = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     ARCHIVO MATANZA.TMAUT
    #     FOR SYSTEM NAME TMAUT
    @property
    def tmAut_Dal(self):
        if self.__tmAut is None:
            try:
                self.__tmAut = self.db.define_table(
                    'TMAUT',
                    Field('DORIGI', type='string', length=8, required=True, label='Dominio Original'),
                    Field('DACTUA', type='string', length=6, required=True, label='Dominio Actual'),
                    Field('FUDDJJ', type='integer', required=True, label='Fech.Ultima DDJJ'),
                    Field('FALTA', type='integer', required=True, label='Fecha Alta'),
                    Field('FTRIBA', type='integer', required=True, label='Fecha Tributación'),
                    Field('MODELO', type='integer', required=True, label='Modelo Año'),
                    Field('TIPOVE', type='string', length=2, required=True, label='Tipo de Vehículo'),
                    Field('USOVEH', type='integer', required=True, label='Uso de Vehículo'),
                    Field('PESO', type='integer', required=True, label='Peso'),
                    Field('CARGA', type='integer', required=True, label='Carga'),
                    Field('CODMAR', type='string', length=7, required=True, label='Código de Marca'),
                    Field('DESFAB', type='string', length=30, required=True, label='Descrip.Fabrica'),
                    Field('DESMOD', type='string', length=60, required=True, label='Descrip.de Modelo'),
                    Field('CODALT', type='string', length=1, required=True, label='Cód.Tipo de Alta'),
                    Field('NACION', type='integer', required=True, label='Nacionalidad'),
                    Field('CATEGO', type='integer', required=True, label='Categoria'),
                    Field('INCISO', type='string', length=1, required=True, label='Inciso'),
                    Field('FEBAJA', type='integer', required=True, label='Fecha de Baja'),
                    Field('COBAJA', type='string', length=1, required=True, label='Código de Baja'),
                    Field('MARMOT', type='string', length=12, required=True, label='Marca de Motor'),
                    Field('SERMOT', type='string', length=12, required=True, label='Serie de Motor'),
                    Field('NORMOT', type='string', length=17, required=True, label='Nro. de Motor'),
                    Field('CHASIS', type='string', length=17, required=True, label='Chasis'),
                    Field('TCOMBU', type='string', length=1, required=True, label='Tipo Combustible'),
                    Field('TYDDOC', type='integer', required=True, label='Tipo de Document.'),
                    Field('NUMDOC', type='integer', required=True, label='Nro.de Documento.'),
                    Field('PROPIE', type='string', length=30, required=True, label='Propietario'),
                    Field('CPFISC', type='integer', required=True, label='Cód.Postal Fiscal'),
                    Field('LOCFIS', type='string', length=17, required=True, label='Localidad Fiscal'),
                    Field('CALFIS', type='string', length=30, required=True, label='Calle  Fiscal'),
                    Field('NROFIS', type='integer', required=True, label='Número Fiscal'),
                    Field('PISFIS', type='string', length=2, required=True, label='Fiscal'),
                    Field('DEPFIS', type='string', length=3, required=True, label='Depto  Fiscal'),
                    Field('TEINFI', type='integer', required=True, label='Tel.Internac.Fisc'),
                    Field('TEZOFI', type='integer', required=True, label='Tel.Zonal Fiscal'),
                    Field('TELFIS', type='string', length=12, required=True, label='Telefono Fiscal'),
                    Field('CUITFI', type='bigint', required=True, label='Cuit Fiscal'),
                    Field('CODPOS', type='integer', required=True, label='Código Postal'),
                    Field('LOCPOS', type='string', length=17, required=True, label='Localidad Postal'),
                    Field('CALPOS', type='string', length=30, required=True, label='Calle  Postal'),
                    Field('NROPOS', type='integer', required=True, label='Número Postal'),
                    Field('PISPOS', type='string', length=2, required=True, label='Piso   Postal'),
                    Field('DEPPOS', type='string', length=2, required=True, label='Depto  Postal'),
                    Field('DESTIN', type='string', length=30, required=True, label='Destinatario'),
                    Field('FCDOMI', type='integer', required=True, label='F.Cambio Dom.Post'),
                    Field('TEINPO', type='integer', required=True, label='Tel.Internac.Post'),
                    Field('TEZOPO', type='integer', required=True, label='Tel.Zonal Postal'),
                    Field('TELPOS', type='string', length=12, required=True, label='Telefono Postal'),
                    Field('CUITPO', type='bigint', required=True, label='Cuit Postal'),
                    Field('CODMUN', type='integer', required=True, label='Código Municipal'),
                    Field('IDENTF', type='string', length=15, required=True, label='Identificador'),
                    Field('IDMUNI', type='integer', required=True, label='Identif.Municipal'),
                    Field('VALUA', type='decimal(17, 2)', required=True, label='Valucion'),
                    Field('FALT', type='integer', required=True, label='Fecha   Alta.....'),
                    Field('HALT', type='integer', required=True, label='Hora    Alta.....'),
                    Field('UALT', type='string', length=10, required=True, label='Usuario Alta.....'),
                    Field('FBAJ', type='integer', required=True, label='Fecha   Baja.....'),
                    Field('HBAJ', type='integer', required=True, label='Hora    Baja.....'),
                    Field('UBAJ', type='string', length=10, required=True, label='Usuario Baja.....'),
                    Field('FMOD', type='integer', required=True, label='Fecha   Modif....'),
                    Field('HMOD', type='integer', required=True, label='Hora    Modif....'),
                    Field('UMOD', type='string', length=10, required=True, label='Usuario Modif....'),
                    Field('FBAJAF', type='integer', required=True, label='Fec. Baj. Fiscal'),
                    Field('FEREVA', type='integer', required=True, label='Fecha Revaluo'),
                    Field('MNECOD', type='integer', required=True, label='Código No Emitir.'),
                    Field('CALCOD', type='integer', required=True, label='Codigo de Calle'),
                    Field('CCLCZO', type='integer', required=True, label='Zona'),
                    Field('TIPDAT', type='string', length=2, required=True, label='AUTO/MOTO'),
                    Field('MCILIN', type='integer', required=True, label='Cilindrada'),
                    primarykey=['IDENTF'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__tmAut
