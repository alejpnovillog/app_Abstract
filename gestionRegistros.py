# Solo se usa el modulo cuando trabajamos con ISERIES
# import pyodbc
try:
    import pyodbc
    from pydal import  DAL, objects
    from pydal.objects import Table
    from pydal.adapters.db2 import DB2Pyodbc

    # ------------------LIBRERIA DE self.constantes
    #import self.constantes
    from app_Config.config import ConfigurarAplicacion
    
    # ------------------LIBRERIA PARA OBTENER LOS DATOS DE CONEXION
    from app_Config.configurarConexion import ConfigHost
    from app_Abstract.allAbstractDB import GxAbstractDb as Gx, SqliteAbstractDb as Sq, ToolsAbatract as Tl, MatanzaAbstractDb as Mtz

except Exception as e:
    print(f'Falta algun modulo {e}')


# --- CLASE DE CONEXION PARA DEFINICIONES ABSTRACTA
class GestionRegistros(Gx, Sq, Tl, Mtz):
    """
    La Clase tiene como objetivo administrar los accesos a la base se datos de Automotores\n
    Esta clase hereda dos clases abstractas GxAbstractDb y SqliteAbstractDb\n
    Parametros:\n
    ambiente =  Determinando este la clase Abstracta que seleccionara\n

    """
    # -- Contructor
    def __init__(self, ambiente=None):

        # Atributos
        self.__ultimoid = None
        self.__ultimoerrorcapturado = None
        self.__ambiente = None
        self.__instancia_Host_Input = None
        self.__dbI = None
        self.__dbValidator = None
        self.__instancia_Host_Input_Dict = None
        self.__instancia_ingresosAbstractDb = None
        self.object_Dal = Table
        self.constantes = ConfigurarAplicacion()

        # Recibimos el Parametro
        # realizamos el setter del atributo ambiente
        self.ambiente = ambiente

        # Generamos la instancia de conexion al Host(server)
        self.get_db()

        # Ejecuto el constructor de la clase heredada ToolsAbstract
        Tl.__init__(self)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Para el caso que el ambiente sea Validator solo toma este 
        # para acceder a una sola clase
        if self.ambiente == self.constantes.ENV_SQ:

            # inicializamos el constructor la clase Sq
            Sq.__init__(self, self.dbI)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # En el caso de que el ambiente no sea Validator inicializa la clase 
        # del Validator Y la clase segun el ambiente
        else:

            # realizamos del setter al atributo dbValidator
            self.dbValidator = self.constantes.ENV_SQ

            # inicializamos el constructor la clase Sq
            Sq.__init__(self, self.dbValidator)

            # si la constante ENV_GX es diferente a None
            if self.constantes.ENV_GX !=None:

                # inicializamos el constructor la clase Gx
                Gx.__init__(self, self.dbI)

            # si la constante ENV_MATANZA es diferente a None
            if self.constantes.ENV_MATANZA != None:

                # inicializamos el constructor la clase Mtz
                Mtz.__init__(self, self.dbI)

    # obtener la descripcion de un atributo de la clase
    def __getattr__(self, item):
        return

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos
    # ---------ULTIMO ID DESPUES DE UN INSERT-----------------------------------
    # getter del atributo  ultimoid
    @property
    def ultimoid(self):
        return self.__ultimoid

    # setter del atributo ultimoid
    @ultimoid.setter
    def ultimoid(self, valor):
        self.__ultimoid = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos
    # ---------ULTIMO ERROR CAPTURADO----------------------------------------
    # getter del atributo ultimoerrorcapturado
    @property
    def ultimoerrorcapturado(self):
        return self.__ultimoerrorcapturado

    # setter del atributo ultimoerrorcapturado
    @ultimoerrorcapturado.setter
    def ultimoerrorcapturado(self, valor):
        self.__ultimoerrorcapturado = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------AMBIENTE DE LA INSTANCIA DEL HOST INPUT--------------------------
    # getter del atributo ambiente
    @property
    def ambiente(self):
        return self.__ambiente

    # setter del atributo ambiente
    @ambiente.setter
    def ambiente(self, valor):
        self.__ambiente = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------INSTANCIA DEL HOST INPUT----------------------------------------
    # getter del atributo instancia_Host_Input
    @property
    def instancia_Host_Input(self):
        return self.__instancia_Host_Input

    # setter del atributo instancia_Host_Input
    @instancia_Host_Input.setter
    def instancia_Host_Input(self, valor):
        self.__instancia_Host_Input = ConfigHost(host=valor)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------DICCIONARIO DE LA INSTANCIA DEL HOST INPUT-----------------------
    # getter del atributo instancia_Host_Input_Dict
    @property
    def instancia_Host_Input_Dict(self):
        return self.__instancia_Host_Input_Dict

    # setter del atributo instancia_Host_Input_Dict
    @instancia_Host_Input_Dict.setter
    def instancia_Host_Input_Dict(self, valor):
        self.__instancia_Host_Input_Dict = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------INSTANCIA DE LA CONEXION A LA INSTANCIA DEL HOST-----------------
    # getter del atributo dbi
    @property
    def dbI(self):
        return self.__dbI

    # setter del atributo dbi
    @dbI.setter
    def dbI(self, valor):
        self.__dbI = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------INSTANCIA DE LA CONEXION A LA INSTANCIA DEL HOSTVALIDATOR--------
    # getter del atributo dbValidador
    @property
    def dbValidator(self):
        return self.__dbI

    # setter del atributo dbValidador
    @dbValidator.setter
    def dbValidator(self, valor):
        self.__dbValidator = valor

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LA INSTACIA DE CONEXION -------------------------------
    def get_db(self):
        """
        Este metodo tiene el objetivo de obtener los datos de conexion del host\n
        del ambiente recibido por parametro\n
        Una vez obtenido el string de conexion se genera un objeto de conexion\n

        """
        try:

            # Genera una instancia de un Host(Servidor)
            # realizamos el setter a self.instancia_Host_Input
            self.instancia_Host_Input = self.ambiente

            # Recibe un diccionario de los datos de conexion de la instancia con
            # realizamos el setter a self.instancia_Host_Input_Dict
            self.instancia_Host_Input_Dict = self.instancia_Host_Input.__datos__()

            # Asigna instancia de conexion a un Handle
            self.dbI = DAL(self.instancia_Host_Input_Dict['strcon'], pool_size=0, db_codec='UTF-8')

        except Exception as e:
            self.ultimoerrorcapturado = e

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS REGISTROS DE UNA TABLA-----------------------------
    # solo se usa la sentencia select es un metodo privado
    def __get_RowsRef(self, tabla, key):
        """
        Realiza la consulta de la tabla \n
        Seleccionando una clave primaria determinada\n
        Recupera en diccionario con los registros incluyendo los campos de las tablas de referencia\n
        """
        try:

            # obtenemos los registros de la tabla donde la columna id =  key    
            rows = self.dbI(tabla._id == key).select()

            # obtiene el diccionario de las filas de la consulta
            registro = rows.records

            # asignamos al diccionario de registros
            rows_dict = registro

            # Verifica que la operacion de lectura haya recuparado registros
            if len(rows_dict) == 0:
                respuesta = {'error': 'NO EXISTE EL REGISTRO'}
            else:
                respuesta = {'error': None}

            # retornamos el diccionario y la respuesta 
            return rows_dict, respuesta

        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return rows_dict, respuesta

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS CAMPOS DE LOS FOREING KEY DE LA TABLA--------------
    # el objetivo es incorporar los campos de las tablas de foreing key
    def tablasRef(self, tabla, registro):

        # Averiguamos si la tabla tiene  tablas de referencias para
        # Foreing key
        for ref in tabla._referenced_by_list:

            # Verificamos si los campos de la tabla de referencia
            # existe en el registro leido
            if ref.fields[0] in registro:

                # Obtenemos el valor de referencia desde el registro Obtenido
                # o sea que no sea nulo
                if registro[ref.fields[0]] != None:

                    # obtenemos el valor y lo tomamos como clave de
                    # busqueda en la tabla de referencia
                    key = registro[ref.fields[0]]

                    # Obtengo el registro de la tabla de referencia con la key
                    registro_ref, respuesta_ref = self.__get_RowsRef(ref, key)

                    # Obtengo el diccionario del registro
                    # de la tabla de referencia con la key
                    registro_ref = registro_ref[0]

                    # Navegamos los campos de la tabla de referencia
                    for f in ref.fields:

                        # Si el campo no esta en el diccionario
                        # del campo registro seleccionado del select
                        if f not in registro:

                            # Agregamos al campo registro
                            # los valores obtenidos de de la tabla de referencia
                            for kmap, vmap in registro_ref.items():
                                registro[f] = vmap[f]

        return registro

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS REGISTROS DE UNA TABLA-----------------------------
    def get_Rows(self, tabla, key):
        """
        Realiza la consulta de la tabla \n
        Seleccionando una clave primaria determinada\n
        Recupera en diccionario con los registros incluyendo los campos de las tablas de referencia\n
        """
        try:

            # obtenemos los registros de la tabla donde la columna id =  key    
            rows = self.dbI(tabla._id == key).select()

            # obtiene el diccionario de las filas de la consulta
            registro = rows.records

            # reasignamos a registros tomando desde registros desde la posicion 0
            registro = registro[0]

            # obtenemos los items
            registro = dict([v for k, v in registro.items()][0])

            # Incorporamos los campos de las Foreing Key al registro
            rows_dict = self.tablasRef(tabla, registro)

            # Verifica que la operacion de lectura haya recuparado registros
            if len(rows_dict) == 0:
                respuesta = {'error': 'NO EXISTE EL REGISTRO'}
            else:
                respuesta = {'error': None}

            # obtenemos los registros y la respuesta
            return rows_dict, respuesta

        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return rows_dict, respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS REGISTROS DE UNA TABLA  CON ALGUNA CONDICION-------
    def get_RowsCondiction(self, tabla, **condicion):
        """
        Realiza la consulta de la tabla por una condicion que debe ser unica\n
        Seleccionando los registros que cumplan una determinada condicion\n
        Recupera en diccionario con los registros incluyendo los campos de las tablas de referencia\n
        """
        try:

            # Tratamiento para APITOKEN
            if tabla._dalname == 'APITOKEN':

                # para el caso que se encuentre dentro de las condiciones
                if condicion['apiregistrosid']:

                    # indicamos que el campo apiregostrosid = al valor de condicion
                    fld1 = tabla.apiregistrosid == condicion['apiregistrosid']

                    # indicamos que el campo apiuserid = al valor de condicion
                    fld2 = tabla.apiuserid ==  condicion['apiuserid']

                    # obtenemos los registros del where del select
                    rows = self.dbI((fld1) & (fld2)).select()
                else:

                    # indicamos que el campo tokenvalor = al valor de condicion
                    fld1 = tabla.tokenvalor == condicion['token']

                    # obtenemos los registros del where del select
                    rows = self.dbI(fld1).select()

            # Tratamiento para APIAUMOSO
            if tabla._dalname == 'APIAUMOSO':

                # para la condicion idpakey
                if condicion['idpakey']:

                    # indicamos que el campo idpakey = al valor de condicion
                    fld1 = tabla.idpakey == condicion['idpakey']

                    # obtenemos los registros del where del select
                    rows = self.dbI(fld1).select()

                # para la condicion reservado
                if condicion['reservado']:

                    # indicamos que el campo samcodbarr = al valor de condicion
                    fld1 = tabla.samcodbarr == condicion['reservado']

                    # obtenemos los registros del where del select
                    rows = self.dbI(fld1).select()


            # Obtengo los registros en un dict
            registro = rows.records

            # Verifica que haya encontrado registros y obtiene los datos de referencia del registro
            if len(registro) != 0:

                # obtenemos los registros incorporando los campos de las tablas de los 
                # campos que son forein key
                rows_dict = self.get_Registros_Ref_Tabla(tabla, *registro)

            # Verifica que la operacion de lectura haya recuparado registros
            if len(rows_dict) == 0:
                respuesta = {'error': 'EL REGISTRO NO ESTA HABILITADO'}
            else:
                respuesta = {'error': None}

            # obtenemos los registros y la respuesta
            return rows_dict, respuesta

        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return rows_dict, respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS REGISTROS DE UNA TABLA-----------------------------
    def get_RowsWhere(self, tabla, **data):
        """
        Realiza la consulta de la tabla \n
        Seleccionando un registro segun los datos de comparacion recibida en data\n
        Recupera en diccionario con los registros incluyendo los campos de las tablas de referencia\n

        :param tabla es el objeto_Dal\n
        :param data es el diccionario donde estan los atributos a seleccionar\n

        :return rows_dict es un diccionario con los registros seleccionados\n
        :return respuesta es un diccionario con las respuesta de la operacion\n
        """
        try:
            rows_dict = {}

            seleciona = None

            # armamos la lista de la clausula where
            listaWhereKey = [k for k, v in data['campos'].items()]

            longLista = len(listaWhereKey)
           
            cantidadRows = 0
            selecciona = None
            tabla
            identificador = int(data['position']['id'])
            desde = int(data['position']['id'])
            cantidad = int(data['position']['read'])
            hasta = desde + cantidad

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Recupera los registros de la tabla recibida
            for rows in self.__dbI((tabla._id >= desde) &(tabla._id <= hasta)).select():

                # Inicializamos las variables
                # registro es el row obtenido
                # i es el id del row obtenido
                registro, i = rows, rows['id']

                # Incorporamos los campos de las Foreing Key al registro
                registro = self.__tablasRef(tabla, registro)

                # Si esta dentro de la lista la clave *all
                # generamos el diccionario de respuesta
                if '*all' in listaWhereKey:
                    selecciona = True
                    rows_dict[i] = registro

                # Si esta dentro de la lista la clave from
                if ('from' in listaWhereKey) and ('count' in listaWhereKey):

                    selecciona = True

                    # Si la cantidad de registros leidos son igual al tope de lectura
                    if cantidadRows == data['count']:
                        break

                    # de lo contrario leo mas registros
                    else:

                        # Averigua si el id del registro es igual al valor desde
                        # el i es el rows['id'] del select
                        if i >= data['from']:
                            rows_dict[i] = registro
                            cantidadRows += 1


                # Si no encuentra la clave en la lista
                if selecciona == None:

                    # Analiza la lista de campos y genera una nueva lista con el analisis
                    # rows es el registro obtenido del select()
                    # data es el diccionario recibido por parametros

                    listaWhere = [True for x in range(0, len(listaWhereKey)) if rows[listaWhereKey[x]] == data[listaWhereKey[x]]]

                    selecciona = None

                    # Navega dentro de la nueva lista generada
                    for x in range(0, len(listaWhere)):

                        if listaWhere[x] == False:
                            selecciona = False
                            break
                        else:
                            selecciona = True
                            rows_dict[i] = registro
                            cantidadRows += 1

            # Verifica que la operacion de lectura haya recuparado registros
            if len(rows_dict) == 0:
                respuesta = {'error': 'NO EXISTE EL REGISTRO'}
            else:
                respuesta = {'error': None}

            # obtenemos los registros y la respuesta
            return rows_dict, respuesta

        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return rows_dict, respuesta

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # -----------OBTENER LA CANTIDAD DE PAGINAS PARA EL HTML 
    # es un metodo privado
    def __createPageParameter(self, **data):

        # determinamos cuantos registros seleccionados por la seleccion
        cuantos = self.db(data['seleccion']).count()

        # obtenemos la cantidad de registros a visualizar en un trabajar con
        # wrkrecords
        if data['wrkrecords']:

            wrkrecords = data['wrkrecords']
        else:

            # obtenemos la constante de la clase 
            wrkrecords = ConfigurarAplicacion.WRK_RECORDS


        # obtenemos cuantas paginas tiene la seleccion de los registros
        hojas = int(cuantos / wrkrecords)

        if hojas == 0:
            hojas = 1

        # obtenemos una lista de los valores desde y hasta de los id de las hojas
        lista = list()
        for i in range(0, hojas):
            if i == 0:
                desde = i + 1
                hasta = desde + 100
            else:
                desde = hasta + 1
                hasta = desde + 100
            lista.append([desde, hasta])

        data['pageno'] = lista

        return data

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # es un metodo privado
    def __createQuery(self, tabla, **data):

        try:
            # aramar el query
            seleccion = False

            # analizamos la lista de data['fieldnumber'] de la constante 
            # LISTA_TABLAS
            for x in data['fieldnumber']:

                # obtenemos el indice del elemento de la lista
                index = data['fieldnumber'].index(x)

                # obtenemos el valor de la lista
                valor = data['field'][index]

                # determina si agrega el operador &
                if data['struct_query'][index] == '&':

                    # para campos numericos
                    if data['op'][index] == 'IN':
                        seleccion &= tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]).belongs(valor)
                    if data['op'][index] == 'EQ':
                        seleccion &= tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) == valor
                    if data['op'][index] == 'LT':
                        seleccion &= tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) <= valor
                    if data['op'][index] == 'GT':
                        seleccion &= tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) >= valor

                # determina que no agregamos algun operador
                else:

                    # para campos alfanumericos o fechas
                    if data['op'][index] == 'EQ':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) == valor
                    if data['op'][index] == 'LK':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]).contains(valor)
                    if data['op'][index] == 'LT':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) < valor
                    if data['op'][index] == 'LE':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) <= valor
                    if data['op'][index] == 'GT':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) > valor
                    if data['op'][index] == 'GE':
                        seleccion = tabla.__getattribute__(tabla._fields[data['fieldnumber'][index]]) >= valor

            # guardamos la seleccion en data
            data['seleccion'] = seleccion

            # retornamos el diccionario data
            return self.__createPageParameter(**data)

        except Exception as e:
            respuesta = {'error': e}
            return respuesta

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def get_rowsWhereWrk(self, tabla, **data):
        """
         recuperamos los registros de la tabla segun una selección
        """
        try:

            # creacion de la query o sea que data['seleccion'] = None
            if not data['seleccion']:
                data = self.__createQuery(tabla, **data)

            # verificamos si tiene cargado el defualt
            if not data['indexpageno']:
                data['indexpageno'] = 0

            # completamos el campo de seleccion
            seleccion = data['seleccion']

            if len(data['pageno'] ) > 1:
                seleccion &= tabla._id >= data['pageno'][data['indexpageno']][0]
                seleccion &= tabla._id <= data['pageno'][data['indexpageno']][1]

            data['seleccion'] = seleccion

            # obtenemos los registros de la seleccion pedida
            rows = self.db(data['seleccion']).select()

            #registro = rows.records
            lista_rows_dict = list()
            rows = rows.records
            for reg in rows:
                #reg = reg[0]

                reg = dict([v for k, v in reg.items()][0])

                # Incorporamos los campos de las Foreing Key al registro
                del reg['update_record']
                del reg['delete_record']

                lista_rows_dict.append(self.tablasRef(tabla, reg))

            # Verifica que la operacion de lectura haya recuparado registros
            if len(lista_rows_dict) == 0:
                respuesta = {'error': 'NO EXISTE EL REGISTRO'}
            else:
                respuesta = {'error': None}

            return lista_rows_dict, respuesta


        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return lista_rows_dict, respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTENER LOS REGISTROS DE LA CABECERA CON SUS DETALLES---------------------------------
    def get_Rows_Cabecera_Detalle(self, tablaDet, tablaCab, key):
        """
        Realiza la consulta de la tabla Automotor Detalle\n
        Recupera en diccionario con los registros\n
        """
        try:
            rows = self.dbI(tablaCab._id == key ).select(join=tablaDet.on(tablaDet.IDAUTOCABECERA == tablaCab._id))
            rows_dict = rows.records

            # Verifica que la operacion de lectura haya recuparado registros
            if len(rows_dict) == 0:
                respuesta = {'error': 'NO EXISTE EL REGISTRO'}
            else:
                respuesta = {'error': None}

            return rows_dict, respuesta

        except Exception as e:
            respuesta = {'error': e}
            self.ultimoerrorcapturado = e
            return rows_dict, respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- GENERAR UN NUEVO REGISTRO DE LA CABECERA--------------------------
    def add_Dal(self, tabla, **campos):
        """
        Realiza el insert de una tabla \n
        Los parametros son:\n
            El object_Dal = objeto tabla\n
            Los campos que es un diccionario con sus valores\n
        Si la operacion de Insert a tenido exito se realiza el commit\n
        De lo contrario se realizara el rollback\n
        """

        try:

            # asignamos el objeto desde la tabla    
            self.object_Dal = tabla

            # obtenemos el ultimo id despues de hacer un insert
            self.ultimoid = self.object_Dal.insert(**campos)

            # realizamos el commit
            self.dbI.commit()

            # retornamos 
            return True
        
        except Exception as e:
            respuesta = e
            self.ultimoerrorcapturado = e
            print(f'Error = {e}')
            print(f'Tabla - {self.object_Dal}')
            print(f'Registro - {campos}')
            self.dbI.rollback()
            return respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- ACTUALIZAR UN REGISTRO DE CABECERA--------------------------
    def upd_Dal(self, tabla, key, **campos):
        """
        Realiza el insert de una tabla \n
        Los parametros son:\n
            El object_Dal = objeto tabla\n
            La Key de acceso a la tabla\n
            Los campos que es un diccionario con sus valores\n
        Si la operacion es realizada correctamente se realizar el Commit\n
        De lo contrario se realizara el rollback\n
        """
        try:

            # asignamos el objeto desde la tabla
            self.object_Dal = tabla

            # actualizamos el objeto tabla
            self.dbI(self.object_Dal._id==key).update(**campos)

            # hacemos permanente los cambios
            self.dbI.commit()

            # retornamos
            return True
        
        except Exception as e:
            respuesta = e
            self.ultimoerrorcapturado = e
            self.dbI.rollback()
            return respuesta

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- ACTUALIZAR UN REGISTRO DE CABECERA--------------------------
    def upd_Lote_Dal(self, tabla, **lote):
        """
        Realiza el update de una tabla \n
        Los parametros son:\n
            El object_Dal = objeto tabla\n
            El lote son los key y los campos que es un diccionario con sus valores\n
        Si la operacion es realizada correctamente se realizar el Commit\n
        De lo contrario se realizara el rollback\n
        """

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Recorre la lista de registros para actualizar
        for l in lote['0']:

            key = l['clave']
            campos = dict()
            campos = l['datos']

            try:
                self.object_Dal = tabla
                self.dbI(self.object_Dal._id==key).update(**campos)

            except Exception as e:
                respuesta = e
                self.ultimoerrorcapturado = e
                self.dbI.rollback()
                return respuesta

        self.dbI.commit()
        return True

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- EJECUCION DE UN COMANDO--------------------------
    def run_comando(self, sql, *parametros):
        """
        Realiza el update de una tabla \n
        Los parametros son:\n
            El sql = sentencia sql\n
            El parametros son los argumentos del sql\n
        """

        try:

            # si hay parametros
            if len(parametros) != 0:

                # ejecutamos la sentencia sql llenando la sentencia con los parametros
                retorno = self.dbI.executesql(sql,  placeholders=parametros)
            else:

                # ejecutamos la sentencia sql sin parametros
                retorno = self.dbI.executesql(sql)

            # aplicamos los cambios    
            self.dbI.commit()


        except Exception as e:
            rtn = {'error':None}
            respuesta = e
            self.ultimoerrorcapturado = e
            rtn['error'] = respuesta
            return rtn

        return retorno

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- OBTIENE LA ESTRUCTURA DE LA TABLA --------------------------
    def get_Struct_Tabla(self, tabla):

        """
        Este metodo permite obtener varios elementos para poder gestionar el objeto tabla\n
                :param objeto_Dal\n
                object_Dal, campos, insert, update, delete\n
                objeto_Dal = Objeto tabla\n
                campos     = los campos del objeto tabla\n
                insert     = el diccionario con los campos a insertar\n
                update     = el diccionario con la clave de la tabla y el registro\n
                delete     = el diccionario con la clave de la tabla\n
        """

        try:

            # Obtiene el diccionario con la estructura
            for k, v in self.getTableTools(tabla).items():
                file, detalle  = k, v

            # Saco de la estructura los datos
            for k, v in detalle.items():

                # si es table asignamos el objeto_Dal el valor de la tabla
                if k == 'table': object_Dal = v

                # si es campos asignamos los campos
                if k == 'campos': campos = v

                # si es insert asignamos el insert
                if k == 'insert': insert = v

                # si es update asignamos update y delete
                if k == 'update': update, delete = v, v

            return object_Dal, campos, insert, update, delete

        except Exception as e:
            self.ultimoerrorcapturado = e

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ---------- INCORPORA AL REGISTRO LOS DATOS DE LAS TABLA DE REFERENCIA DE LA TABLA ----------------
    def get_Registros_Ref_Tabla(self, tabla, *registro):

        try:

            # Definicion de la lista temporaria y final de todas las tablas de referencias
            lista_temp, lista_final = list(), list()

            # Primer elemento de la lista temporaria
            lista_temp.append(tabla)

            # Agregamos la tablas de referencia del primer nivel
            lista_temp = self.tabla._referenced_by_list

            # Señal para corte del lopp
            haymas = False

            # Hacemos un lopp
            while True:

                # Recorremos la lista temporaria de las tablas de referencia
                for ref in lista_temp:

                    # Averiguamos si la tabla NO EXISTE en la lista final de tablas
                    if ref not in lista_final:
                        haymas = True

                        # Recorremos las tablas de referencia del elemento ref
                        for r in ref._referenced_by_list:

                            # Averiguamos si NO EXISTE en la lista temporal
                            if r not in lista_temp:
                                lista_temp.append(r)

                        # Al finalizar el reccorrido de por la lista de referencia del elemento ref
                        # agregamos un elemento a la tabla final
                        lista_final.append(ref)

                        haymas = False

                # la señal haymas esta en false sale del loop
                if haymas == False:
                    break


            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Ahora debemos insertar los campos y sus valores en el registro final a devolver

            # Inicializamos indices
            ir, fk, i = 0, 0, 0

            # Analisamos la lista de las tablas de referencia de la tabla recibida
            for ref in lista_final:

                # Verificamos si los campos de la tabla de referencia existe en el registro leido
                if ref.fields[i] in registro[ir][tabla._tablename]:

                    # Obtenemos el valor de referencia desde el registro Obtenido
                    if registro[ir][tabla._tablename][ref.fields[i]] != None:

                        # armamos la clave de acceso
                        key = registro[ir][tabla._tablename][ref.fields[fk]]

                        # Obtengo el registro de la tabla de referencia con la key
                        registro_ref, respuesta_ref = self.get_Rows(ref, key)

                        # Obtengo el diccionario del registro de la tabla de referencia con la key
                        registro_ref = registro_ref[ir]

                        # Navegamos los campos de la tabla recibida de referencia
                        for f in ref.fields:

                            # Si el campo no esta en el diccionario del campo registro
                            if f not in registro[ir][tabla._tablename]:

                                # Agregamos al campo registro los valores obtenidos del registro de la tabla de referencia
                                for kmap, vmap in registro_ref.items():
                                    registro[ir][tabla._tablename][f] = vmap[f]

            #-----------------------------------------------------------------------------------

            return registro

        except Exception as e:
            self.ultimoerrorcapturado = e
