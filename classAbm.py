# -------Lista de lisbrerias y Modulos
try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


# Abm tablas
class AbmTablas():
    """
    TIENE DOS PARAMETROS:\n
    ges =  es el gestor de tablas de un ambiente determinado del motor de bases de datos\n\n
    idtabla = es el id de la tabla
    dbslate = es el id dela tabla esclava
    objetoTabla =  Es un objeto tabla para realizar su gestion\n
    que esta en el motor  del ambiente seleccionado\n\n
    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor con los argumentos para hacer la gestion ABM de tablas
    def __init__(self, **argumentos):

        # recepcion de los parametros

        # objeto de conexion
        self.__ges = argumentos['ges']

        # objeto tabla
        self.__idtabla = argumentos['objeto_dal']

        # objeto tabla esclava
        self.__dbslate = argumentos['dbslate']

        # lista de tablas del sistema donde tiene parametros de funcionalidad        
        self.__listaTablas = ConfigurarAplicacion.LISTA_TABLAS

        # Recupera los elemento de gestin del idtabla
        self.__getObjetoTabla()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo campos
    @property
    def campos(self):
        return self.__campos

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo insert
    @property
    def insert(self):
        return self.__insert

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo update
    @property
    def update(self):
        return self.__update

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # getter del atributo delete
    @property
    def delete(self):
        return self.__delete

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtengo un registr de una tabla con un where de algunos 
    # campos de su regitro
    def getRecordCondition(self, **condicion):
        """
        Pasa un parametro\n
        condicion = es un dict con los campos a realizar la operacion\n
        Retorna 2 parametro:\n
        dict un diccionario con el registro seleccionado si lo hubiera\n\n
        dict un diccionario con el error si lo hubiera\n\n

        """
        try:

            # Realiza la Consulta
            return self.__ges.get_RowsCondiction(self.__objetoTabla, **condicion)

        except Exception as e:
            print(f'Error - getRecordCondition {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Insert Registro 
    def insertRecord(self, **data):
        """
        Pasa un parametro\n
        data = es un dict con los campos a realizar la operacion\n
        Retorna 1 parametro:\n
        dict un diccionario con el error si lo hubiera\n\n
        """
        try:

            # Realiza el Insert
            return self.__ges.add_Dal(self.__objetoTabla, **data)

        except Exception as e:
            print(f'Error - insertRecord {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Update Registro
    def updateRecord(self, **data):
        """
        Pasa un parametro\n
        data = es un dict con los campos a realizar la operacion\n
        Retorna 1 parametro:\n
        dict un diccionario con el error si lo hubiera\n\n
        """
        try:

            # obtenemos la clave
            key = data['clave']

            # obtenemos los datos a actualizar
            datadict = data['datos']

            # Realiza el Update
            return self.__ges.upd_Dal(self.__objetoTabla, data['clave'], **data['datos'])

        except Exception as e:
            print(f'Error - updateRecord {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Update Registro por Lotes
    def updateRecordLote(self, **data):

        """
        Pasa un parametro\n
        data = es un dict con los campos a realizar la operacion\n
        Retorna 1 parametro:\n
        dict un diccionario con el error si lo hubiera\n\n
        """
        try:

            # Realiza el Update en Lote
            return self.__ges.upd_Lote_Dal(self.__objetoTabla, **data)

        except Exception as e:
            print(f'Error - updateRecordLote {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # get Registro Exacto
    def getRecord(self, **data):
        """
        Pasa un parametro\n
        data = es un dict con los campos a realizar la operacion\n
        Retorna 2 parametro:\n
        dict un diccionario con el registro seleccionado si lo hubiera\n\n
        dict un diccionario con el error si lo hubiera\n\n

        """
        try:

            # Realiza la Consulta
            return self.__ges.get_Rows(self.__objetoTabla, data['clave'])

        except Exception as e:
            print(f'Error - getRecord {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # get Registro con una clausula Where
    def getRecordWhere(self, **data):
        """
        Pasa un parametro\n
        data = es un dict con los campos a realizar la operacion\n
        (para el caso de querer seleccionar todos los registros de la tabla {'*all': '*all'.upper()})\n

        Retorna 2 parametro:\n
        dict un diccionario con el registro seleccionado si lo hubiera\n\n
        dict un diccionario con el error si lo hubiera\n\n

        """
        try:

            # Campos que no hay que tener encuenta dentro del row recibido
            lista_key = ['id', 'update_record', 'delete_record']

            # variables de trabajo
            data_dict, data_list = dict(), list()

            # Realiza la Consulta al objeto tabla segun el where que se le envia en el diccionario data
            datos, errores = self.__ges.get_RowsWhere(self.__objetoTabla, **data)

            # Verifica si hay algun error
            if errores['error'] is None:

                # Navegamos por los rows recibidos
                # k es el id del registro de la tabla
                # v es el diccionario del registro recuperado
                for k, v in datos.items():
                    data_dict = dict()

                    # Navegamos por el contenido del rows
                    # kd es el nombre del campo del registro
                    # vd es el contenido del campo del registro
                    for kd, vd in dict(v).items():

                        # Si el valor obtenido no esta en la lista Key
                        if kd not in lista_key:

                            # incorporo al diccionario
                            data_dict[kd] = vd

                    # Generamos la lista de los registros
                    data_list.append(data_dict)

            # retornamos la lista de registros obtenidos si no hay error
            # si hay error la lista de registros esta vacia
            return data_list, errores

        except Exception as e:
            print(f'Error - getRecordWhere {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtener instancia de Objeto Tabla con los atributos de objetoTabla, 
    # campos, insert, update, delete
    def __getObjetoTabla(self):

        try:

            # Recorre la lista de tablas del config
            # k es el nombre de la tabla en la clase config
            # v es el diccionario con el numero y su nombre del atributo 
            # de la clase gestionRegistros
            for k, v in self.__listaTablas.items():

                # obtenemos el diccionario de la lista
                elemento = self.__listaTablas[k]

                # verificamos si el idtabla es igual al valor del item numero
                if self.__idtabla == elemento['numero']:

                    # obtengo la estructura del la tabla
                    # __getattribute__(elemento['objeto']) se obtiene el atributo de la clase
                    # gestionRegistros
                    tabla = self.__ges.__getattribute__(elemento['objeto'])
                    self.__objetoTabla, self.__campos, self.__insert, self.__update, self.__delete = self.__ges.get_Struct_Tabla(tabla)

                    return

        except Exception as e:
            print(f'Error - __getObjetoTabla {e}')
