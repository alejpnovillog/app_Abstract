# -------Lista de lisbrerias y Modulos
try:

    # librería para definición de los campos
    from pydal import  Field

    # acceso a la clase
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Atributos del Esquema Matanza
class AtributosMatanza():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor
    def __init__(self):
        pass

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla Maut
    def tablaMaut(self):
        """
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

        """

        try:

            lista, primary, parm = list(), list(), dict()

            # fields list
            lista = [
                Field('DORIGI', type='string', length=8, required=True, comment='Dominio Original'),
                Field('DACTUA', type='string', length=6, required=True, comment='Dominio Actual'),
                Field('FUDDJJ', type='integer', required=True, comment='Fecha Ult DDJJ'),
                Field('FALT',   type='integer', required=True, comment='Fecha Alta'),
                Field('FTRIBA', type='integer', required=True, comment='Fecha Tributacion'),
                Field('MODELO', type='integer', required=True, comment='Año Modelo'),
                Field('TIPOVE', type='string', length=2, required=True, comment='Tipo Vehiculo'),
                Field('USOVEH', type='integer', required=True, comment='Uso Vehiculo'),
                Field('PESO',   type='integer',  required=True, comment='Peso'),
                Field('CARGA',  type='integer', required=True, comment='Carga'),
                Field('CODMAR', type='string', length=7, required=True, comment='Codigo Marca'),
                Field('DESFAB', type='string', length=30, required=True, comment='Descr. Fabrica'),
                Field('DESMOD', type='string', length=60, required=True, comment='Descr. Modelo'),
                Field('CODALT', type='string', length=1, required=True, comment='Cod Tipo Alta'),
                Field('NACION', type='integer', required=True, comment='Nacionalidad'),
                Field('CATEGO', type='integer', required=True, comment='Categoria'),
                Field('INCISO', type='string', length=1, required=True, comment='Inicio'),
                Field('FBAJ',   type='integer', required=True, comment='Fecha Baja'),
                Field('COBAJA', type='string', length=1, required=True, comment='Cod Baja'),
                Field('MARMOT', type='string', length=12, required=True, comment='Marca Motor'),
                Field('SERMOT', type='string', length=12, required=True, comment='Serie Motor'),
                Field('NORMOT', type='string', length=17, required=True, comment='Numero Motor'),
                Field('CHASIS', type='string', length=17, required=True, comment='Nro Chasis'),
                Field('TCOMBU', type='string', length=1, required=True, comment='Tipo Combustible'),
                Field('TYDDOC', type='integer', required=True, comment='Tipo Documento'),
                Field('NUMDOC', type='integer', required=True, comment='Nro Documento'),
                Field('PROPIE', type='string', length=30, required=True, comment='Propietario'),
                Field('CPFISC', type='integer', required=True, comment='Cod Postal Fiscal'),
                Field('LOCFIS', type='string', length=17, required=True, comment='Localidad Fiscal'),
                Field('CALFIS', type='string', length=30, required=True, comment='Calle Fiscal'),
                Field('NROFIS', type='integer', required=True, comment='Nro Fiscal'),
                Field('PISFIS', type='string', length=2, required=True, comment='Piso Fiscal'),
                Field('DEPFIS', type='string', length=3, required=True, comment='Depto Fiscal'),
                Field('TEINFI', type='integer', required=True, comment='Tel Internacional Fiscal'),
                Field('TEZOFI', type='integer', required=True, comment='Tel Zona Fiscal'),
                Field('TELFIS', type='string', length=12,   required=True, comment='Telefono Fiscal'),
                Field('CUITFI', type='bigint', required=True, comment='Cuit Fiscal'),
                Field('CODPOS', type='integer', required=True, comment='Codigo Postal'),
                Field('LOCPOS', type='string', length=17, required=True, comment='Localidad Postal'),
                Field('CALPOS', type='string', length=30, required=True, comment='Calle Postal'),
                Field('NROPOS', type='integer', required=True, comment='Nro Postal'),
                Field('PISPOS', type='string', length=2, required=True, comment='Piso Postal'),
                Field('DEPPOS', type='string', length=2, required=True, comment='Depto Postal'),
                Field('DESTIN', type='string', length=30, required=True, comment='Destinatario'),
                Field('FCDOMI', type='integer', required=True, comment='Fecha Camb Domicilio Postal'),
                Field('TEINPO', type='integer', required=True, comment='Tel Internacional Postal'),
                Field('TEZOPO', type='integer', required=True, comment='Tel Zona Postal'),
                Field('TELPOS', type='string', length=12,   required=True, comment='Telefono Fostal'),
                Field('CUITPO', type='bigint', required=True, comment='Cuit Postal'),
                Field('CODMUN', type='integer', required=True, comment='Cod Municipal'),
                Field('IDENTF', type='string', length=15,   required=True, comment='Identificador'),
                Field('IDMUNI', type='integer', required=True, comment='Id Municipal'),
                Field('VALUA', type='decimal(17, 2)', required=True, comment='Valuacion'),
                Field('FALT',   type='integer', required=True, comment='Fecha Alta'),
                Field('HALT',   type='integer', required=True, comment='Hora Alta'),
                Field('UALT',   type='string', length=10,   required=True, comment='Usuario Alta'),
                Field('FBAJ',   type='integer', required=True, comment='Fecha Baja'),
                Field('HBAJ',   type='integer', required=True, comment='Hora Baja'),
                Field('UBAJ',   type='string', length=10,   required=True, comment='Usuario Baja'),
                Field('FMOD',   type='integer', required=True, comment='Fecha Modificacion'),
                Field('HMOD',   type='integer', required=True, comment='Hora Modificacion'),
                Field('UMOD',   type='string', length=10,   required=True, comment='Usuario Modificacion'),
                Field('FBAJAF', type='integer', required=True, comment='Fecha Baja Fiscal'),
                Field('FEREVA', type='integer', required=True, comment='Fecha Revaluo'),
                Field('MNECOD', type='integer', required=True, comment='Cod No Emitir'),
                Field('CALCOD', type='integer', required=True, comment='Cod Calle'),
                Field('CCLCZO', type='integer', required=True, comment='Zona'),
                Field('TIPDAT', type='string', length=2, required=True, comment='Auto Moto'),
                Field('MCILIN', type='integer', required=True, comment='Cilindrada')
                ]

            # Primary Key list
            primary = [
                'IDENTF'
            ]

            # table construction parameters
            parm = {
                'name': 'TMAUT',
                'fields': tuple(lista),
                'arg': {'primarykey': primary, 'migrate': False},
                'sqlfldtexto': True
            }

            return parm

        except Exception as e:
            print(f'Error - AtributosMatanza tablaMaut {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Atributos del Esquema GxProd
class AtributosGx():

    def __init__(self):
        pass


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Impresion Pdf
    def tablaImpresionPdf(self):
            """
            PDF PRINT TABLE DEFINITION \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
            """
            try:

                # fields list
                lista = [
                    Field('IMPRESIONID', type='id', comment='Id'),
                    Field('IMPRESIONPRMUNO', type='string', length=512, required=True, comment='Param Impresion Uno'),
                    Field('IMPRESIONPRMDOS', type='string', length=512, required=True, comment='Param Impresion Dos'),
                    Field('IMPRESIONUSUARIO', type='string', length=10, required=True, comment='Impresion Usuarios'),
                    Field('IMPRESIONFECHA', type='datetime', required=True, comment='Fecha Impresion')
                    ]

                # table construction parameters
                parm = {
                     'name': 'IMPRESIONPDF',
                     'fields': tuple(lista),
                     'arg': {'migrate': False},
                     'sqlfldtexto': True
                 }

                return parm

            except Exception as e:
                print(f'Error - tablaImpresionPdf {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Mensajes Error Msg Dinamicos
    def tablaMensajesErrorMsgDinamicos(self):
        """
        DYNAMIC ERROR MESSAGE TABLE DEFINITION \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:

            # fields list
            lista = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje'),
                Field('MSGDINAMICOID', type='integer', required=True, comment='Id FK Msg Dinamico'),
                Field('MSGDINAMICOLEN', type='integer', required=True, comment='Long Msg Dinamico')
                ]

            # Primary Key list
            primary = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje'),
                Field('MSGDINAMICOID', type='integer', required=True, comment='Id FK Msg Dinamico')
            ]

            # table construction parameters
            parm = {
                 'name': 'MENSAJESERRORMSGDINAMICOS',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaMensajesErrorMsgDinamicos {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Mensajes Error
    def tablaMensajesError(self):
        """
        DEFINITION OF THE ERROR MESSAGE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:

            # fields list
            lista = [
                Field('MSGCODE', type='string', length=7,    required=True, comment='Cod Mensaje'),
                Field('MSGDESCRIPCION', type='string', length=150,  required=True, comment='Descr Mensaje'),
                Field('MSGHELP', type='string', length=1024, required=True, comment='Mensaje Ayuda'),
                Field('NIVELGRAVEDADID', type='reference MSGNIVELGRAVEDAD', ondelete='CASCADE', comment='Id FK Nivel Gravedad')
                ]

            # Primary Key list
            primary = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje')
            ]

            # table construction parameters
            parm = {
                 'name': 'MENSAJESERROR',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaMensajesError {e}')


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Nivel de Gravedad
    def tablaNivelGravedad(self):

        try:

            # fields list
            lista = [
                Field('NIVELGRAVEDADID',  type='id', comment='Id'),
                Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50,   required=True, comment='Descr Nivel Gravedad'),
                Field('MSGNIVELGRAVEDADALERTA',   type='string', length=50,   required=True, comment='Alerta Nivel Gravedad')
                ]

            # table construction parameters
            parm = {
                 'name': 'MSGNIVELGRAVEDAD',
                 'fields': tuple(lista),
                 'arg': {'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaNivelGravedad {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Atributos para Sucerp
class AtributosSucerp():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor 
     def __init__(self):
         pass

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Registro
     def tablaTipoRegistro(self):

        """
             DEFINITION OF THE RECORD TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:
             # elementos para la definicion de una tabla   
             lista, primary, parm = list(), list(), dict()

             # lista de campos de la tabla
             lista = [
                 Field('tiporegistroid', type='id', comment='Id'),
                 Field('tiporegistro', unique=True, type='string', length=2, required=True, comment='Tipo Registro'),
                 Field('desctiporegistro', unique=True, type='string', length=50, required=True, comment='Desc Tipo Registro')
            ]

             # obtenemos el flag para saber si crea la tabla o no
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_REGISTRO']['migrate']

             # parametro para la construccion de la tabla
             parm = {
                 'name' :  'TIPOREGISTRO',
                 'fields' :  tuple(lista),
                 'arg' :  {'migrate': migrate},
                 'sqlfldtexto' : True
            }

             return parm

        except Exception as e:
            print(f'Error - tablaTipoRegistro {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Sub Registro
     def tablaTipoSubRegistro(self):
         """
         DEFINITION OF THE SUBREGISTRY TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tiposubregistroid', type='id', comment='Id'),
                 Field('tiposubregistro', unique=True, type='string', length=1, required=True, comment='Tipo Sub Registro'),
                 Field('desctiposubregistro', unique=True, type='string', length=50, required=True, comment='Descr Tipo Sub Registro')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_SUB_REGISTRO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOSUBREGISTRO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoSubRegistro {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Cuerpo
     def tablaTipoCuerpo(self):
         """
         BODY TYPE TABLE DEFINITION\n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipocuerpoid', type='id', comment='Id'),
                 Field('tipocuerpo', unique=True,  type='string', length=2,    required=True, comment='Tipo Cuerpo'),
                 Field('desctipocuerpo', unique=True, type='string', length=50, required=True, comment='Desc Cuerpo')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUERPO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOCUERPO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoCuerpo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Titular
     def tablaTipoTitular(self):
         """
         DEFINITION OF THE HOLDER TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipotitularid', type='id', comment='Id'),
                 Field('tipotitular', unique=True, type='string', length=1,    required=True, comment='Tipo Tirular'),
                 Field('desctipotitular', unique=True, type='string', length=50, required=True, comment='Desc Tipo Titular')
                 ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_TITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Origen
     def tablaTipoOrigen(self):
         """
         DEFINITION OF THE TYPE OF ORIGIN TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('origenid', type='id', comment='Id'),
                 Field('tipoorigen', unique=True, type='string', length=1, required=True, comment='Origen'),
                 Field('descorigen', unique=True, type='string', length=50, required=True, comment='Desc Origen')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_ORIGEN']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOORIGEN',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoOrigen {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Movimiento
     def tablaTipoMovimiento(self):
         """
         DEFINITION OF THE MOVEMENT TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('codigotipomovimientoid', type='id', comment='Id'),
                 Field('codigotipomovimiento', unique=True,  type='integer', required=True, comment='Codigo Tipo Movimiento'),
                 Field('desctipomovimiento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Movimiento')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_MOVIMIENTO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOMOVIMIENTO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoMovimiento {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Forma de Pago
     def tablaTipoPago(self):
         """
         DEFINITION OF THE PAYMENT TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('codigoformapagoid', type='id', comment='Id'),
                Field('codigoformapago', unique=True, type='integer', required=True, comment='Codigo Forma Pago'),
                Field('descrtipopago', unique=True, type='string', length=50, required=True, comment='Desc Tipo Pago')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_PAGO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOPAGO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm


         except Exception as e:
                print(f'Error - tablaTipoPago {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Moneda
     def tablaTipoMoneda(self):

         """
         DEFINITION OF THE CURRENCY TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('codigomonedaid', type='id', comment='Id'),
                Field('codigomoneda', unique=True, type='integer', required=True, comment='Codigo Moneda'),
                Field('desctipomoneda', unique=True, type='string', length=50, required=True, comment='Desc Tipo Moneda')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_MONEDA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOMONEDA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoMoneda {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Documento
     def tablaTipoDocumento(self):

         """
         DEFINITION OF THE DOCUMENT TYPE TABLE\n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # Lista de campos
             lista = [
                Field('tipodocumentoid', type='id', comment='Id'),
                Field('tipodocumento', unique=True, type='integer', required=True, comment='Tipo Documento'),
                Field('desctipodocumento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Documento')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_DOCUMENTO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPODOCUMENTO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoDocumento {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Provincias
     def tablaProvincias(self):

         """
         DEFINITION OF THE TABLE OF PROVINCES \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('provinciaid', type='id', comment='Id'),
                Field('provincia', unique=True, type='integer', required=True, comment='Provincia'),
                Field('descprovincia', unique=True, type='string', length=50, required=True, comment='Desc Provincia')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROVINCIA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'PROVINCIAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaProvincias {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Estado
     def tablaEstado(self):

         """
         DEFINITION OF THE STATE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fileds list
             lista = [
                 Field('estadoid', type='id', comment='Id'),
                 Field('estado', unique=True,      type='string', length=1,    required=True, comment='Estado'),
                 Field('descestado', unique=True, type='string', length=50, required=True, comment='Desc Estado')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ESTADO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOESTADO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaEstado {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tipo de Cuota
     def tablaTipoCuota(self):

         """
         DEFINITION OF THE FEE TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipocuotaid', type='id', comment='Id'),
                 Field('tipocuota', unique=True, type='integer', required=True, comment='Tipo Cuota'),
                 Field('desctipocuota', unique=True,  type='string', length=50, required=True, comment='Desc Tipo Cuota')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUOTA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOCUOTA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoCuota {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Encabezado No tiene Id porque no va ser una tabla sql
     def tablaEncabezado(self):

         """
         DEFINITION OF THE HEADER TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('encabezadoid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('versionprotocolo', type='string', length=5,    required=True, comment='Version Protocolo'),
                Field('revisionprotocolo', type='string', length=5,    required=True, comment='Revision Protocolo'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('numeroenvio', type='bigint', required=True, comment='Nro Envio'),
                Field('fechahora', type='datetime', required=True, comment='Fecha Hora'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ENCABEZADO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ENCABEZADO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaEncabezado {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva No tiene Id porque no va ser una tabla sql
     def tablaAltaImpositiva(self):

         """
         DEFINITION OF THE HIGH TAX TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('altataxid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('numerotramite', type='bigint',  required=True, comment='Nro Tramite'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                Field('marca', type='string', length=60, required=True, comment='Marca'),
                Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
                Field('modelo', type='string', length=100, required=True, comment='Modelo'),
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                Field('peso', type='integer', required=True, comment='Peso'),
                Field('carga', type='integer', required=True, comment='Carga'),
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
                Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
                Field('registroseccionalorigen', type='integer', required=True, comment='Registro Seccion Origen'),
                Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz Soc Reg Seccional Origeb'),
                Field('municipalidadorigen', type='string', length=150,  required=True, comment='Municipalidad Origen'),
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Parm Adicionales'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
                Field('altataxtitularid', type='reference ALTAIMPOSITIVATITULAR', ondelete='CASCADE', comment='Id FK Alta Impositiva Titular'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ALTAIMPOSITIVA']['migrate']

             # table construction parameters
             parm = {
                'name': 'ALTAIMPOSITIVA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAltaImpositiva {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Arba and Sucerp Brand Relationship Table
     def tablaRelArbaSucerpMarca(self):

         """
         DEFINITION OF THE ARBA SUCERP BRAND RELATIONSHIP TABLE\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # field list
             lista = [
                 Field('relArbaSucerpid', type='id', comment='Id'),
                 Field('relArbaSucerpArba', type='string', length=10, required=True, comment='Arba'),
                 Field('relArbaSucerpMarca', type='string', length=60, required=True, comment='Marca'),
                 Field('relArbaSucerpModelo', type='string', length=60, required=True, comment='Modelo'),
                 Field('relArbaSucerpCodMtmFmm', type='string', length=8, required=True, comment='Sucerp'),
                 Field('relArbaSucerpInciso', type='string', length=4, required=True, comment='Inciso'),
                 Field('relArbaSucerpEstado', type='string', length=1, required=True, comment='1=Procesa, 0=A Confirmar'),
                 Field('relArbaSucerpOrigenDato', type='string', length=1, required=True, comment='Origen Dato'),
                 Field('relArbaSucerpMarcaMoto', type='string', length=60, required=True, comment='Marca Moto'),
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_RELACION_ARBA_SUCERP_MARCA']['migrate']

             parm = {
                'name': 'RELACIONARBASUCERPMARCA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }
             return parm

         except Exception as e:
             print(f'Error - tablaRelArbaSucerpMarca {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Procesos de Importacion y Exportacion
     def tablaProcesoImportacionExportacion(self):

         """
         DEFINITION OF IMPORTEXPORT PROCESS TABLE\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # field list
             lista = [
                 Field('procesoid', type='id', comment='Id'),
                 Field('procesocodigotabla', type='integer', required=True, comment='Proceso Codigo Tabla'),
                 Field('procesonombretabla', type='string', length=150, required=True, comment='Proceso Nombre Tabla'),
                 Field('procesotransferencia', type='string', length=1, required=True, comment='Transferencia (S, Nulo)'),
                 Field('procesofechatransferencia', type='datetime',  comment='Fecha Transferencia'),
                 Field('procesobasedatos', type='string', length=1, required=True, comment='Base Datos (S, Nulo)'),
                 Field('procesofechabasedatos', type='datetime',  comment='Fecha Base Datos'),
                 Field('procesoaccion', type='string', length=1, required=True, comment='Accion ( E, I, Nulo)'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROCESOIMPORTACIONEXPORTACION']['migrate']

             parm = {
                'name': 'PROCESOIMPORTACIONEXPORTACION',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }
             return parm

         except Exception as e:
             print(f'Error - tablaRelArbaSucerpMarca {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva Titular No tiene Id porque no va ser una 
     # tabla sql
     def tablaAltaImpositivaTitular(self):

         """
         DEFINITION OF THE HOLDER'S HIGH TAX TABLE \n
         WE RETURN:\n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('altataxtitularid', type='id', comment='Id'),
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                 Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                 Field('calle', type='string', length=40, required=True, comment='Calle'),
                 Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                 Field('piso', type='string', length=10, required=True, comment='Piso'),
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                 Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                 Field('codigopostal', type='string', length=8, required=True, comment='Cod Postal'),
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincia'),
                 Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
                 Field('ktimestamp', type='datetime', required=True, comment='Timestamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ALTAIMPOSITIVATITULAR']['migrate']

            # table construction parameters
             parm = {
                 'name': 'ALTAIMPOSITIVATITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAltaImpositivaTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Baja Impositiva No tiene Id porque no va ser una tabla sql
     def tablaBajaImpositiva(self):

         """
         DEFINITION OF THE TAX LOW TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

              # fields list
             lista = [
                 Field('bajataxid', type='id', comment='Id'),
                 Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Registro'),
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 Field('codigoorganismo', type='integer', required=True, comment='Cod Organismo'),
                 Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                 Field('codigotipotramite', type='integer', required=True, comment='Cod Tipo Tramite'),
                 Field('descrtipotramite', type='string', length=60, required=True, comment='Descripcion Tramite'),
                 Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
                 Field('descrtipoaccion', type='string', length=60, required=True, comment='Descripcion Tipo Accion'),
                 Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                 Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                 Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                 Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                 Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                 Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id Fk Tipo Origen'),
                 Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                 Field('marca', type='string', length=60, required=True, comment='Marca'),
                 Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                 Field('modelo',  type='string', length=100,  required=True, comment='Modelo'),
                 Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                 Field('peso', type='integer', required=True, comment='Peso Vehiculo'),
                 Field('carga', type='integer', required=True, comment='Carga'),
                 Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                 Field('valuacion', type='integer', required=True, comment='Valuacion'),
                 Field('codigotipouso', type='string', length=2,    required=True, comment='Cod Tipo Uso'),
                 Field('descrtipouso', type='string', length=100,  required=True, comment='Descripcion Tipo Uso'),
                 Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                 Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                 Field('codigoregistronacional', type='integer', required=True, comment='Codigo Registro  Nacional'),
                 Field('razonsocial', type='string', length=40,   required=True, comment='Razon Social'),
                 Field('registroseccionaldestino', type='integer', required=True, comment='Registro Seccional Destino'),
                 Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz. Soc. Reg. Seccional  Orig.'),
                 Field('municipalidaddestino', type='string', length=150,  required=True, comment='Muni. Destino'),
                 Field('fechaoperacion', type='datetime', required=True, comment='Fecha Operacion'),
                 Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Param. Adicionales'),
                 Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                 Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
                 Field('bajataxtitularid', type='reference BAJAIMPOSITIVATITULAR', ondelete='CASCADE', comment='Id Fk Baja Impositiva Titular'),
                 Field('ktimestamp', type='datetime', required=True, comment='Key TimeStamp'),
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_BAJAIMPOSITIVA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'BAJAIMPOSITIVA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaBajaImpositiva {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva Titular No tiene Id porque no va ser una 
     # tabla sql
     def tablaBajaImpositivaTitular(self):

         """
         DEFINITION OF THE HOLDER'S LOW TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n
         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('bajataxtitularid', type='id', comment='Id'),
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
                 Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
                 Field('calle', type='string', length=40, required=True, comment='Calle'),
                 Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                 Field('piso', type='string', length=10, required=True, comment='Piso'),
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                 Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                 Field('codigopostal', type='string', length=8,    required=True, comment='Cod Postal'),
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincias'),
                 Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
                 Field('ktimestamp', type='datetime', required=True, comment='Timestamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_BAJAIMPOSITIVATITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'BAJAIMPOSITIVATITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaBajaImpositivaTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos No tiene Id porque no va ser una tabla sql
     def tablaImpuestosSellos(self):

         """
         DEFINITION OF THE STAMP TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('taxsellosid', type='id', comment='Id'),
                 Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                 Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                 Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                 Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
                 Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr. Tipo Accion'),
                 Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                 Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                 Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                 Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo' ),
                 Field('recibo', type='string', length=15, required=True, comment='Recibo'),
                 Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                 Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                 Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                 Field('marca', type='string', length=60,   required=True, comment='Marca'),
                 Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                 Field('modelo',  type='string', length=100,  required=True, comment='Modelo'),
                 Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                 Field('codigotipouso',            type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
                 Field('descrtipouso',             type='string', length=100,  required=True, comment='Descr Tipo Uso'),
                 Field('valuacion', type='integer', required=True, comment='Valuacion'),
                 Field('cantidadpartes', type='integer', required=True, comment='Cantidad Partes'),
                 Field('montoimpuestoadicional', type='decimal(12, 2)',      required=True, comment='Monto Impuesto Adicional'),
                 Field('montopunitorios',          type='decimal(12, 2)',      required=True, comment='Monto Punitorios'),
                 Field('montototalcobrado',        type='decimal(12, 2)',      required=True, comment='Monto Total Cobrado'),
                 Field('montoabonado',             type='decimal(12, 2)',      required=True, comment='Monto Abonado'),
                 Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                 Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                 Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                 Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
                 Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
                 Field('exencion',                 type='string', length=1,    required=True, comment='Execcion'),
                 Field('codigoexencion',           type='string', length=10,   required=True, comment='Codigo Execcion'),
                 Field('descripcionexencion',      type='string', length=100,  required=True, comment='Descr Execcion'),
                 Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
                 Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                 Field('cuitregistroseccional',   type='bigint',              required=True, comment='Cuit Registro Seccional'),
                 Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
                 Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                 Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Parm Adicionales'),
                 Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                 Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
                 Field('observacionesanulacion', type='string', length=256,  required=True, comment='Observaciones Anulacion'),
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellos {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos Partes No tiene Id porque no va ser una 
     # tabla sql
     def tablaImpuestosSellosPartes(self):

         """
         PART STAMP TAX TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('taxsellospartesid', type='id', comment='Id'),
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                 Field('tipointerviniente', type='integer', required=True, comment='Tipo Interviniente'),
                 Field('descrtipointerviniente', type='string', length=60,   required=True, comment='Descr Tipo Interviniente'),
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
                 Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                 Field('calle', type='string', length=40,   required=True, comment='Calle'),
                 Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
                 Field('piso', type='string', length=10,   required=True, comment='Piso'),
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                 Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                 Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                 Field('exencion', type='string', length=1,    required=True, comment='Execcion'),
                 Field('codigoexencion', type='string', length=10,   required=True, comment='Codigo Execcion'),
                 Field('descripcionexencion', type='string', length=100,  required=True, comment='Descr Execcion'),
                 Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                 Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                 Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOSPARTES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOSPARTES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellosPartes {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos Partes Tipo Tramite No tiene Id porque 
     # no va ser una tabla sql
     def tablaImpuestosSellosPartesTipoTramite(self):

         """
         DEFINITION OF THE TAX TABLE OF PARTS STAMPS BY TYPE OF PROCESS\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('taxsellospartestipotramiteid', type='id', comment='Id'),
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                Field('montocontrato', type='decimal(12, 2)', required=True, comment='Monto Contrato'),
                Field('baseimponible', type='decimal(12, 2)', required=True, comment='Base Imponible'),
                Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
                Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
                Field('montofueraregistro', type='decimal(12, 2)', required=True, comment='Monto Abonado Fuera Registro'),
                Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
                Field('alicuota', type='decimal(5, 2)', required=True, comment='Alicuota'),
                Field('porcentajecontrato', type='decimal(5, 2)', required=True, comment='Porcentaje Contrato'),
                Field('porcentajeimpuesto', type='decimal(5, 2)', required=True, comment='Porcentaje Impuesto'),
                Field('fechacontrato', type='datetime', required=True, comment='Fecha Contrato'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOSPARTESTIPOTRAMITE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellosPartesTipoTramite {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuesto  Automotor No tiene Id porque no va ser una tabla sql
     def tablaImpuestoAutomotor(self):

         """
         DEFINITION OF THE AUTOMOTIVE TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('taxautomotorid', type='id', comment='Id'),
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                Field('codigotipomovimientoid', type='reference TIPOMOVIMIENTO', ondelete='CASCADE', comment='Id FK Cod Tipo Movimiento'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                Field('yyyy', type='integer', required=True, comment='Año'),
                Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
                Field('fechabonificacion', type='date', required=True, comment='Fecha Bonificacion'),
                Field('fechavencimiento', type='date', required=True, comment='Fecha Vencimiento'),
                Field('flagvencimiento', type='string', length=1, required=True, comment='Flag Vencimiento'),
                Field('importebonificado', type='decimal(10, 2)', required=True, comment='Importe Bonificado'),
                Field('importecomun', type='decimal(10, 2)', required=True, comment='Importe Comun'),
                Field('fechaproceso', type='datetime', required=True, comment='Fecha Proceso'),
                Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
                Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
                Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
                Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
                Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
                Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
                Field('fechatransferencia', type='datetime', required=True, comment='Fecha Transferencia'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOAUTOMOTOR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOAUTOMOTOR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaImpuestoAutomotor {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Vehiculo No tiene Id porque no va ser una 
     # tabla sql
     def tablaInformacionVehiculo(self):

         """
          DEFINITION OF THE VEHICLE INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('infvehiculoid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                Field('peso', type='integer', required=True, comment='Peso'),
                Field('carga', type='integer', required=True, comment='Carga'),
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
                Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
                Field('fechainscripcioninicial', type='date', required=True, comment='Fecha Inscripcion Inicial'),
                Field('fechaultimatransferencia', type='date', required=True, comment='Fecha Ult Transferencia'),
                Field('fechaultimomovimiento', type='date', required=True, comment='Fecha Ult Movimiento'),
                Field('estadodominial', type='string', length=1,    required=True, comment='Estado Dominial'),
                Field('fechacambioestadodominal', type='date', required=True, comment='Fecha Camb Estado Dominial'),
                Field('guardahabitual', type='string', length=1,    required=True, comment='Guarda Habitual'),
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('controlsucerp', type='string', length=3,    required=True, comment='Control Sucerp'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIONVEHICULO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIONVEHICULO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionVehiculo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Vehiculo del Titular No tiene Id porque no va ser 
     # una tabla sql
     def tablaInformacionVehiculoTitular(self):

         """
          DEFINITION OF THE HOLDER'S VEHICLE INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('infvehiculotitularid', type='id', comment='Id'),
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', notnull=False, comment='Id FK Inf Vehiculo'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIONVEHICULOTITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIONVEHICULOTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionVehiculoTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Temporal Informacion de Vehiculo No tiene Id porque no va ser 
     # una tabla definida con DDS
     def tablaTmpInformacionVehiculo(self):

         """
          TEMPORARY VEHICLE INFORMATION TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('INFVE00001', type='integer', comment='Id'),
                 Field('TIPOR00001', type='integer', comment='Id FK Tipo Cuerpo'),
                 Field('TIPOS00001', type='integer', comment='Id FK Tipo Documento'),
                 Field('CODIG0ORGA', type='integer', comment='Codigo Organismo'),
                 Field('DOMIN00001', type='string', length=8, comment='Dominio Nuevo'),
                 Field('DOMIN00002', type='string', length=8, comment='Dominio Viejo'),
                 Field('CODMTMFNM1', type='string', length=8, comment='Codigo Sucerp'),
                 Field('ORIGENID01', type='integer', comment='Id FK Origen'),
                 Field('CATEG00001', type='string', length=3, comment='Categoria'),
                 Field('MARCA00001', type='string', length=60, comment='Marca'),
                 Field('TIPOV00001', type='string', length=60, comment='Tipo Vehiculo'),
                 Field('MODEL00001', type='string', length=100, comment='Modelo'),
                 Field('YYYYM00001', type='integer', comment='Año Modelo'),
                 Field('PESO_00001', type='integer', comment='Peso'),
                 Field('CARGA00001', type='integer', comment='Carga'),
                 Field('CILIN00001', type='integer', comment='Cilindrada'),
                 Field('VALUA00001', type='integer', comment='Valuacion'),
                 Field('CODIG00003', type='string', length=2, comment='Codigo Tipo Uso'),
                 Field('DESCR00001', type='string', length=100, comment='Descr Tipo Uso'),
                 Field('FECHA00001', type='date', comment='Fecha Inscripcion Inicial'),
                 Field('FECHA00002', type='date', comment='Fecha Ult Transferencia'),
                 Field('FECHA00003', type='date', comment='Fecha Ult Movimiento'),
                 Field('ESTAD00001', type='string', length=1, comment='Estado Dominial'),
                 Field('FECHA00004', type='date', comment='Fecha Camb Estado Dominial'),
                 Field('GUARD00001', type='string', length=1, comment='Guarda Habitual'),
                 Field('CALLE00001', type='string', length=40, comment='Calle'),
                 Field('NUMER00002', type='string', length=10, comment='Nro Puerta'),
                 Field('PISO_00001', type='string', length=10, comment='Piso'),
                 Field('DEPAR00001', typr='string', length=10, comment='Depto'),
                 Field('BARRI00001', type='string', length=40, comment='Barrio'),
                 Field('LOCAL00001', type='string', length=40, comment='Localidad'),
                 Field('CODIG00004', type='string', length=8, comment='Codigo Postal'),
                 Field('PROVI00001', type='integer', comment='Id FK Provincia'),
                 Field('CANTI00001', type='integer', comment='Cantidad Titulares'),
                 Field('CODIG00005', type='integer', comment='Codigo Registro Seccional'),
                 Field('RAZON00001', type='string', length=40, comment='Razon Social'),
                 Field('FECHA00005', type='datetime', comment='fecha Operacion'),
                 Field('RESER00001', type='string', length=256, comment='Reservado'),
                 Field('CONTR00001', type='string', length=3, comment='Control Sucerp'),
                 Field('KTIME00001', type='datetime', comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULO']['migrate']

             # Primary Key List
             primary = ['INFVE00001']

             # table construction parameters
             parm = {
                 'name': 'INFOR00001',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTmpInformacionVehiculo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Temporal Informacion de Vehiculo Titular No tiene Id porque no 
     # va ser una tabla definida con DDS
     def tablaTmpInformacionVehiculoTitular(self):

         """
          DEFINITION OF THE INFORMATION TABLE OF THE TEMPORARY OWNER VEHICLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('INFVE00003', type='integer', comment='Id'),
                 Field('TIPOC00001', type='integer', comment='Id FK Tipo Cuerpo'),
                 Field('TIPOS00001', type='integer', comment='Id FK Tipo Sub Registro'),
                 Field('TIPOD00001', type='integer', comment='Id FK Tipo Documento'),
                 Field('NUMER00001', type='integer', comment='Nro Documento'),
                 Field('CUITC00001', type='integer', comment='Cuit/Cuil'),
                 Field('APELL00001', type='string', length=150, comment='Apellido y Nombre'),
                 Field('PORCE00001', type='integer', comment='Porcentaje Titular'),
                 Field('CALLE00001', type='string', length=40, comment='Calle'),
                 Field('NUMER00002', type='string', length=10, comment='Nro Puerta'),
                 Field('PISO_00001', type='string', length=10, comment='Piso'),
                 Field('DEPAR00001', type='string', length=10, comment='Depto'),
                 Field('BARRI00001', type='string', length=40, comment='Barrio'),
                 Field('LOCAL00001', type='string', length=40, comment='Localidad'),
                 Field('CODIG00001', type='string', length=8, comment='Codigo Postal'),
                 Field('PROVI00001', type='integer', comment='Id FK Provincia'),
                 Field('RESER00001', type='string', length=256, comment='Reservado'),
                 Field('INFVE00002', type='integer', comment='Id FK Inf Vehiculo'),
                 Field('KTIME00001', type='detetime', comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULOTITULAR']['migrate']

             # Lista de Primary Key
             primary = ['INFVE00003']

             # table construction parameters
             parm = {
                 'name': 'INFOR00002',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaTmpInformacionVehiculoTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Cambio de Titularidad No tiene Id porque no va ser una tabla sql
     def tablaCambioTitularidad(self):
         """
          DEFINITION OF THE CHANGE OF OWNERSHIP TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('cambiotitularidadid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                Field('marca', type='string', length=60, required=True, comment='Marca'),
                Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
                Field('modelo', type='string', length=100, required=True, comment='Modelo'),
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                Field('peso', type='integer', required=True, comment='Peso'),
                Field('carga', type='integer', required=True, comment='Carga'),
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
                Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apenomrazonsocial', type='string', length=150, required=True, comment='ApeNom Razon Social'),
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('razonsocial', type='string', length=40, required=True, comment='Razon Social'),
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                Field('parametrosadicionales', type='string', length=650, required=True, comment='Parm Adicionales'),
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                Field('observaciones', type='string', length=256, required=True, comment='Observaciones'),
                Field('cambiotitularidadtitid', type='reference CAMBIOTITULARIDADTITULAR', ondelete='CASCADE', comment='Id FK Camb Titularidad Titu'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_CAMBIOTITULARIDAD']['migrate']

             # table construction parameters
             parm = {
                 'name': 'CAMBIOTITULARIDAD',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaCambioTitularidad {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Cambio de Titularidad Titular No tiene Id porque no va ser una 
     # tabla sql
     def tablaCambioTitularidadTitular(self):

         """
          DEFINITION OF THE TABLE OF CHANGE OF OWNERSHIP OF THE HOLDER \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('cambiotitularidadtitid', type='id', comment='Id'),
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_CAMBIOTITULARIDADTITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'CAMBIOTITULARIDADTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaCambioTitularidadTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Radicacion No tiene Id porque no va ser una 
     # tabla sql
     def tablaInformacionRadicacion(self):

         """
          DEFINITION OF THE FILING INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('infradicacionid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('dominio', type='string', length=8,    required=True, comment='Dominio'),
                Field('estadoid', type='reference TIPOESTADO',  ondelete='CASCADE', comment='Id FK Estado'),
                Field('tiporadicacion', type='string', length=1,    required=True, comment='Tipo Radicacion'),
                Field('fechaalta', type='date', required=True, comment='Fecha Alta'),
                Field('fechabajaradicacion', type='date', required=True, comment='Fecha Baja Radicacion'),
                Field('origeninformacion', type='string', length=1,    required=True, comment='Origen Informacion'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('razonsocialregistro', type='string', length=100,  required=True, comment='Razon Social Registro'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIORADICACION']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIORADICACION',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionRadicacion {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Anulacion de Tramites de Sellos No tiene Id porque no va ser una 
     # tabla sql
     def tablaAnulacionTramitesSellos(self):

         """
          DEFINITION OF THE TABLE FOR CANCELLATION OF STAMP PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('anultramitesellosid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('tipoanulacion',            type='string', length=1,    required=True, comment='Tipo Anulacion'),
                Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                Field('numerorecibo',             type='string', length=15,   required=True, comment='Nro Recibo'),
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                Field('montototal',               type='decimal(12, 2)',      required=True, comment='Monto Total'),
                Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
                Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
                Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
                Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
                Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
                Field('fechatramite', type='datetime', required=True, comment='Fecha Tramite'),
                Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
                Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
                Field('fechabaja', type='date', required=True, comment='Fecha Baja'),
                Field('cantidaddetalle', type='integer', required=True, comment='Cantidad Detalle'),
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ANULACIONTRAMITESSELLOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ANULACIONTRAMITESSELLOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAnulacionTramitesSellos {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Anulacion de Tramites de Sellos Detalle No tiene Id porque no va 
     # ser una tabla sql
     def tablaAnulacionTramitesSellosDetalle(self):

         """
          DETAILED DEFINITION OF THE TABLE FOR CANCELLATION OF STAMP PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('anultramitesellosdetid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('yyyy', type='integer', required=True, comment='Año'),
                Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
                Field('tipocuotaid', type='reference TIPOCUOTA', ondelete='CASCADE', comment='Id FK Tipo Cuota'),
                Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
                Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
                Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
                Field('importeadicional',         type='decimal(10, 2)',      required=True, comment='Importe Adicional'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
                Field('anultramitesellosid', type='reference ANULACIONTRAMITESSELLOS', ondelete='CASCADE', comment='Id FK Anulacion Tramites Sellos'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ANULACIONTRAMITESSELLOSDETALLE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ANULACIONTRAMITESSELLOSDETALLE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAnulacionTramitesSellosDetalle {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tramites Generales No tiene Id porque no va ser una tabla sql
     def tablaTramitesGenerales(self):

         """
          DEFINITION OF THE TABLE OF GENERAL PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields  list
             lista = [
                Field('tramitesgeneralesid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                Field('peso', type='integer', required=True, comment='Peso'),
                Field('carga', type='integer', required=True, comment='Carga'),
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
                Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                Field('tramitesgeneralestitid', type='reference TRAMITESGENERALESTITULARES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TRAMITESGENERALES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TRAMITESGENERALES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTramitesGenerales {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tramites Generales Titulares No tiene Id porque no va ser 
     # una tabla sql
     def tablaTramitesGeneralesTitulares(self):

         """
          DEFINITION OF THE TABLE OF GENERAL PROCEDURES FOR HOLDERS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('tramitesgeneralestitid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TRAMITESGENERALESTITULARES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TRAMITESGENERALESTITULARES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTramitesGeneralesTitulares {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Pie No tiene Id porque no va ser una tabla sql
     def tablaPie(self):

         """
          DEFINITION OF THE FOOT BOARD \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('pieid', type='id', comment='Id'),
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                Field('cantidadregistros', type='integer', required=True, comment='Cantidad Regsitros'),
                Field('checksum',                 type='string', length=32,   required=True, comment='Check Sum'),
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
                ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PIE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'PIE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaPie {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla para Responder al Api
     def tablaApiAumoso(self):

         """
          DEFINITION OF THE AUMOSO TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('aumosoid', type='id', comment='Id'),
                Field('idpakey', type='bigint', required=True, comment='IdPakey'),
                Field('samnrodoc', type='bigint', required=True, comment='Sam Nro Documento'),
                Field('samcuit', type='bigint', required=True, comment='Sam Cuit'),
                Field('samareages', type='bigint', required=True, comment='Sam Area Gestion'),
                Field('samdareages', type='string', length=100,  required=True, comment='Sam Descr Area Gestion'),
                Field('idcontrib', type='string', length=15,   required=True, comment='Id FK Contrib'),
                Field('samcontmu', type='bigint', required=True, comment='Sam Cont Mu'),
                Field('samaaocuo', type='integer', required=True, comment='Sam Año Cuota'),
                Field('samcuota', type='string', length=2,    required=True, comment='Sam Cuota'),
                Field('samtasa', type='integer', required=True, comment='Sam Tasa'),
                Field('samdtasa', type='string', length=100,  required=True, comment='Desc Sam Tasa'),
                Field('samconvenio', type='integer', required=True, comment='Sam Convenio'),
                Field('samimporte', type='decimal(15, 2)',      required=True, comment='Sam Importe'),
                Field('samfecvto', type='date', required=True, comment='Sam Fecha Vencimiento'),
                Field('samintpuni', type='decimal(15, 2)', required=True, comment='Sam Intereses Punitorios'),
                Field('samintresa', type='decimal(15, 2)', required=True, comment='Sam Intresa'),
                Field('samrecargo', type='decimal(15, 2)', required=True, comment='Sam Recargo'),
                Field('samfeccal', type='date', required=True, comment='Sam Fecha Calculo'),
                Field('samimpboni', type='decimal(15, 2)', required=True, comment='Sam Importe Bonificado'),
                Field('samfevtbon', type='date', required=True, comment='Sam Fecha Venc Bonificacion'),
                Field('samcodbarr', type='string', length=50, required=True, comment='Sam Cod Barra'),
                Field('tokenapiid', type='reference APITOKEN', ondelete='CASCADE', comment='Id FK Token Api'),
                Field('cuotacancelada',  type='string', length=1,    required=True, default='N', comment='Cuota Cancelada'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_AUMOSO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIAUMOSO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiAumoso {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Estados para Responder al Api
     def tablaApiEstados(self):

         """
          API STATE TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apiestadosid', type='id', comment='Id'),
                Field('apiestadodescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Estado'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_ESTADOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIESTADOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstados {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Log de Errores del Apí
     def tablaApiLog(self):

         """
          API LOG TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apilogid', type='id',  comment='Id'),
                Field('apilogerror', type='string', length=15360, required=True, comment='Json del Error'),
                Field('apilogtimestamp', type='datetime', required=True, comment='Error Log Time Stamp'),
                Field('apilogidcontrib', type='string', length=15, required=True, comment='Id Contribuyente Aumoso'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_LOG']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APILOG',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiLog {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Archivos Recibidos de Sucerp
     def tablaRecepcionArchivos(self):

         """
          DEFINITION OF THE FILE RECEPTION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('archivorecibidoid', type='id', comment='Id'),
                Field('archivonombre', unique=True, type='string', length=256, required=True, comment='Nombre Archivo'),
                Field('archivousercrt',   type='string', length=10,  required=True, comment='Archivo User Create'),
                Field('archivoprocesado', type='datetime', required=True, comment='Archivo Procesado'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_RECEPCIONARCHIVOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'RECEPCIONARCHIVOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstados {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Tareas para Responder al Api
     def tablaApiTareas(self):

         """
          TASK API TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apitareasid', type='id', comment='Id'),
                Field('apitareasdescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Tareas'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TAREAS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITAREAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiTareas {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Estados Tareas para Responder al Api
     def tablaApiEstadosTareas(self):

         """
          DEFINITION OF THE API TABLE STATES TASKS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apiestadotareasid', type='id', comment='Id'),
                Field('apiestadosid', type='reference APIESTADOS', ondelete='CASCADE', comment='Id FK Token Api Estado'),
                Field('apitareasid', type='reference APITAREAS', ondelete='CASCADE', comment='Id FK Token Api Tareas'),
                Field('apiestadosnewid', type='reference APIESTADOS', ondelete='CASCADE', comment='Id FK Token Estado New'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_ESTADOS_TAREAS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIESTADOSTAREAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstadosTareas {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token Registros para Responder al Api
     def tablaApiRegistros(self):

         """
          API TABLE DEFINITION REGISTERS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('apiregistrosid', type='id', comment='Id'),
                Field('apiregistrosdescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Registros'),
                Field('apiregistrosnumero', unique=True, type='integer', required=True, comment='Token Api Registros Nro'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_REGISTROS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIREGISTROS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaApiRegistros {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token Usuario para Responder al Api
     def tablaApiTokenUser(self):

         """
          DEFINITION OF THE USERS API TOKEN TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('apiuserid', type='id', comment='Id'),
                Field('apiusernombre', unique=True, type='string', length=10, required=True, comment='Token Api User Nombre'),
                Field('apiuserpass', type='password', length=10, required=True, comment='Token Api User Pass'),
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                Field('apiuseremail', unique=True, type='string', length=256, required=True, comment='Token Api User Email'),
                Field('apiuserwhatsapp', unique=True, type='string', length=20, required=True, default='', comment='Token Api User Whatsapp'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint',  comment='Nro Documento'),
                Field('apiregistrosid', type='reference APIREGISTROS', ondelete='CASCADE', comment='Id FK Token Api Registros'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('apiusercrt', type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt', type='string', length=10,   comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime',  comment='Token Api User Dlt Time Stamp'),

             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN_USER']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITOKENUSER',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaApiTokenUser {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token para Responder al Api
     def tablaApiToken(self):

         """
          API TOKEN TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('tokenapiid', type='id',  comment='Id'),
                Field('tokenvalor', unique=True,  type='string', length=512,  required=True, comment='Token Valor'),
                Field('apiuserid', type='reference APITOKENUSER', ondelete='CASCADE', comment='Id FK Token Api User'),
                Field('tokentimestamp', type='datetime', required=True, comment='Token Time Stamp'),
                Field('apiregistrosid', type='reference APIREGISTROS', ondelete='CASCADE', comment='Id FK Token Api Registros'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('tokenconectar', type='boolean', required=True, default='0', comment='Token Conectar'),
                Field('tokeniniciotransaccion', type='boolean', required=True, default='0', comment='Token Inicio Transaccion'),
                Field('tokenfintransaccion', type='boolean', required=True, default='0', comment='Token Fin Transaccion'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITOKEN',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiToken {e}')
