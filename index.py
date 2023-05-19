# -------Lista de lisbrerias y Modulos
try:

    from flask import Flask, render_template, url_for
    from flask import jsonify, request, redirect
    #from flask_weasyprint import HTML, render_pdf
    import copy

    # Tratamiento de Flask para los mail
    #from flask_mail import Mail
    #from flask_mail import Message

    # Tratamiento de Pdf
    #from pdfkit.pdfkit import PDFKit
    #import pdfkit

    #from werkzeug.datastructures import ImmutableMultiDict

    from app_Config.config import ConfigurarAplicacion

    # Clases para menejar la aplicacion
    from app_Request import classRequest

    from app_Formularios.datos_Formularios import form0001

except Exception as e:
    print(f'Falta algun modulo {e}')


# GENERO LA INSTANCIA
app = Flask('__name__')

# configuramos la instancia de flask app 
app.config.from_object(ConfigurarAplicacion)

# Asignamos una instancia de la clase pasandole el server http
formulario = form0001(app.config['SERVER_HTTP_DEVELOPMENT'])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Funcion de renderizacion de paginas Wrk
def render_rtn(lista, pagina, **error):

    # Verificamos si hay un error
    if error['error'] != None:

        # redirecciono a un pagina de respuesta
        return redirect(url_for('.respuesta'))

    # Para el caso si no hay error
    else:

        # Hacia donde se renderiza
        if app.config['SWITCH_RENDER_TEMPLATE'] == False:

            # Retorna un json
            return jsonify(lista)

        else:

            # Renderizo el Html
            return render_template(pagina, datos=lista)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Funcion de renderizacion de paginas Upd
def render_update(pagina, **datos):

    # Verificamos si hay un error
    if datos['errores'] != True:

        # redirecciono a un pagina de respuesta
        return redirect(url_for('.respuesta'))

    # Para el caso si no hay error
    else:

        # Hacia donde se renderiza
        if app.config['SWITCH_RENDER_TEMPLATE'] == False:

            # Retorna un json
            return jsonify(datos['errores'])

        else:

            # Renderizo el Html
            return render_template(pagina, datos=datos['formato'])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tratamiento la carga del combobox
# retorna una lista con el contenido para el combobox
def slt_comobobox(cursor, **template):

    # Inicializacion
    lista_new = list()

    # Obtengo el diccionario del cursor dentro del diccionario 
    # estan los campos del registro
    for cursor_dict in cursor:

        for kr, vr in cursor_dict.items():

            # Verifica si la clave esta en el template
            if kr.upper() in template:
                contenido = template[kr.upper()]
                contenido['value'] = vr
                template[kr.upper()] = contenido

        # Genera un nuevo miembro de la lista
        lista_new.append(copy.deepcopy(template))

    return lista_new


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON ESTADOS
@app.route('/estadowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/estadowrk/<int:id>/<int:qry>', methods=['GET'])
def estadoawrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_ESTADO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipoestadowrkhlp(*data_list), app.config['HTML_WRKESTADOS'], **errores)

#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON PROVINCIAS - PROBADO
@app.route('/provinciawrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/provinciawrk/<int:id>/<int:qry>', methods=['GET'])
def provinciawrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_PROVINCIA'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.provinciawrkhlp(*data_list), app.config['HTML_WRKPROVINCIAS'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE CUERPOS - PROBADO
@app.route('/tipocuerpowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipocuerpowrk/<int:id>/<int:qry>', methods=['GET'])
def tipocuerpowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_CUERPO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipocuerpowrkhlp(*data_list), app.config['HTML_WRKTIPOCUERPO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE CUOTA - PROBADO
@app.route('/tipocuotawrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipocuotawrk/<int:id>/<int:qry>', methods=['GET'])
def tipocuotawrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_CUOTA'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipocuotawrkhlp(*data_list), app.config['HTML_WRKTIPOCUOTA'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE DOCUMENTOS - PROBADO
@app.route('/tipodocumentowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipodocumentowrk/<int:id>/<int:qry>', methods=['GET'])
def tipodocumentowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_DOCUMENTO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipodocumentowrkhlp(*data_list), app.config['HTML_WRKTIPODOCUMENTO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE MONEDA
@app.route('/tipomonedawrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipomonedawrk/<int:id>/<int:qry>', methods=['GET'])
def tipomonedawrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_MONEDA'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipomonedawrkhlp(*data_list), app.config['HTML_WRKTIPOMONEDA'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE MOVIMIENTO
@app.route('/tipomovimientowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipomovimientowrk/<int:id>/<int:qry>', methods=['GET'])
def tipomovimientowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_MOVIMIENTO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipomovimientowrkhlp(*data_list), app.config['HTML_WRKTIPOMOVIMIENTO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE ORIGEN
@app.route('/tipoorigenwrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipoorigenwrk/<int:id>/<int:qry>', methods=['GET'])
def tipoorigenwrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_ORIGEN'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipoorigenwrkhlp(*data_list), app.config['HTML_WRKTIPOORIGEN'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE PAGO
@app.route('/tipopagowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipopagowrk/<int:id>/<int:qry>', methods=['GET'])
def tipopagowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_PAGO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipopagowrkhlp(*data_list), app.config['HTML_WRKTIPOPAGO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE REGISTRO
@app.route('/tiporegistrowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tiporegistrowrk/<int:id>/<int:qry>', methods=['GET'])
def tiporegistrowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_REGISTRO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tiporegistrowrkhlp(*data_list), app.config['HTML_WRKTIPOREGISTRO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE SUB REGISTRO
@app.route('/tiposubregistrowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tiposubregistrowrk/<int:id>/<int:qry>', methods=['GET'])
def tiposubregistrowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_SUB_REGISTRO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tiposubregistrowrkhlp(*data_list), app.config['HTML_WRKTIPOSUBREGISTRO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON TIPO DE TITULAR
@app.route('/tipotitularwrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/tipotitularwrk/<int:id>/<int:qry>', methods=['GET'])
def tipotitularwrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_TITULAR'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tipotitularwrkhlp(*data_list), app.config['HTML_WRKTIPOTITULAR'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON API TOKEN USER - PROBADO
@app.route('/apitokenuserwrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/apitokenuserwrk/<int:id>/<int:qry>', methods=['GET'])
def apitokenuserwrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TOKEN_USER'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.tokenuserwrkhlp(*data_list), app.config['HTML_WRKAPITOKENUSER'], **errores)

#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON API ESTADOS - PROBADO
@app.route('/apiestadoswrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/apiestadoswrk/<int:id>/<int:qry>', methods=['GET'])
def apiestadoswrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_ESTADOS'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.apiestadoswrkhlp(*data_list), app.config['HTML_WRKAPIESTADOS'], **errores)

#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON API TAREAS - PROBADO
@app.route('/apitareaswrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/apitareaswrk/<int:id>/<int:qry>', methods=['GET'])
def apitareaswrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TAREAS'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.apitareaswrkhlp(*data_list), app.config['HTML_WRKAPITAREAS'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON API TOKEN - PROBADO
@app.route('/apitokenwrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/apitokenwrk/<int:id>/<int:qry>', methods=['GET'])
def apitokenwrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TOKEN'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.apitokenwrkhlp(*data_list), app.config['HTML_WRKAPITOKEN'], **errores)

#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON API AUMOSO
@app.route('/apiaumosowrk/<int:id>', defaults={'qry': 0}, methods=['GET'])
@app.route('/apiaumosowrk/<int:id>/<int:qry>', methods=['GET'])
def apiaumosowrk(id, qry):

    # Recupera todos los registros
    data_list, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_AUMOSO'])

    # Retorna la informacion al Usuario
    return render_rtn(formulario.apiaumosowrkhlp(*data_list), app.config['HTML_WRKAPIAUMOSO'], **errores)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UNA PROVINCIA
@app.route('/provinciaadd/', methods=['GET', 'POST'])
def provinciaadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_PROVINCIA'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.provinciaaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDPROVINCIAS'], datos=formulario.provinciaaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE CUERPO
@app.route('/tipocuerpoadd/', methods=['GET', 'POST'])
def tipocuerpoadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_CUERPO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipocuerpoaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOCUERPO'], datos=formulario.tipocuerpoaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE CUOTA
@app.route('/tipocuotaadd/', methods=['GET', 'POST'])
def tipocuotaadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_CUOTA'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipocuotaaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOCUOTA'], datos=formulario.tipocuotaaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE DOCUMENTO
@app.route('/tipodocumentoadd/', methods=['GET', 'POST'])
def tipodocumentoadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_DOCUMENTO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipodocumentoaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPODOCUMENTO'], datos=formulario.tipodocumentoaddhlp())

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE ESTADO
@app.route('/tipoestadoadd/', methods=['GET', 'POST'])
def tipoestadoadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_ESTADO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipoestadoaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOESTADO'], datos=formulario.tipoestadoaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE MONEDA
@app.route('/tipomonedaadd/', methods=['GET', 'POST'])
def tipomonedaadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_MONEDA'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipomonedaaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOMONEDA'], datos=formulario.tipomonedaaddhlp())

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE MOVIMIENTO
@app.route('/tipomovimientoadd/', methods=['GET', 'POST'])
def tipomovimientoadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_MOVIMIENTO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipomovimientoaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOMOVIMIENTO'], datos=formulario.tipomovimientoaddhlp())

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE ORIGEN
@app.route('/tipoorigenadd/', methods=['GET', 'POST'])
def tipoorigenadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_ORIGEN'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipoorigenaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOORIGEN'], datos=formulario.tipoorigenaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE PAGO
@app.route('/tipopagoadd/', methods=['GET', 'POST'])
def tipopagoadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_PAGO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipopagoaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOPAGO'], datos=formulario.tipopagoaddhlp())

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE REGISTRO
@app.route('/tiporegistroadd/', methods=['GET', 'POST'])
def tiporegistroadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_REGISTRO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tiporegistroaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOREGISTRO'], datos=formulario.tiporegistroaddhlp())

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE SUB REGISTRO
@app.route('/tiposubregistroadd/', methods=['GET', 'POST'])
def tiposubregistroadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_SUB_REGISTRO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tiposubregistroaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOSUBREGISTRO'], datos=formulario.tiposubregistroaddhlp())



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN TIPO DE TITULAR
@app.route('/tipotitularadd/', methods=['GET', 'POST'])
def tipotitularadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de provincia
        errores = classRequest.requestAdd(app.config['TABLA_TIPO_TITULAR'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tipotitularaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDTIPOTITULAR'], datos=formulario.tipotitularaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN API DE ESTADOS
@app.route('/apiestadosadd/', methods=['GET', 'POST'])
def apiestadosadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de api de estados
        errores = classRequest.requestAdd(app.config['TABLA_API_ESTADOS'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.apiestadosaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDAPIESTADOS'], datos=formulario.apiestadosaddhlp())




#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN API DE TAREAS
@app.route('/apitareasadd/', methods=['GET', 'POST'])
def apitareasadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de api de estados
        errores = classRequest.requestAdd(app.config['TABLA_API_TAREAS'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.apitareasaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDAPITAREAS'], datos=formulario.apitareasaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN API DE REGISTROS
@app.route('/apiregistrosadd/', methods=['GET', 'POST'])
def apiregistrosadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de api de registros
        errores = classRequest.requestAdd(app.config['TABLA_API_TOKEN_REGISTRO'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.apiregistrosaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    return render_template(app.config['HTML_ADDAPIREGISTROS'], datos=formulario.apiregistrosaddhlp())


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN API DE TOKEN USER
@app.route('/tokenuseradd/', methods=['GET', 'POST'])
def tokenuseradd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Realizamos el insert el registro de api de registros
        errores = classRequest.requestAdd(app.config['TABLA_API_TOKEN_USER'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.tokenuseraddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Recupera todos los registros
    qry = 0
    id = 0
    data_list_tipo_documentos, errores = classRequest.requestWrk(id, qry, app.config['TABLA_TIPO_DOCUMENTO'])

    # Recupera todos los registros
    data_list_api_registros, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TOKEN_REGISTRO'])

    # Obtenemos el diccionario con la estructura para enviar al front-end
    datos = formulario.tokenuseraddhlp()

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tratamiento de el select de tipo de movimiento
    datos_sltdocumentos = copy.deepcopy(datos['add']['SLTTIPODOCUMENTO'][0])
    datos['add']['SLTTIPODOCUMENTO'].clear()

    # Procesamos la lista de tipo de documentos
    lista_nueva = slt_comobobox(data_list_tipo_documentos, **datos_sltdocumentos)
    datos['add']['SLTTIPODOCUMENTO'] = lista_nueva

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tratamiento de el select de registros
    datos_sltregistros = copy.deepcopy(datos['add']['SLTAPIREGISTROS'][0])
    datos['add']['SLTAPIREGISTROS'].clear()

    # Procesamos la lista de los api de registros
    lista_nueva = slt_comobobox(data_list_api_registros, **datos_sltregistros)
    datos['add']['SLTAPIREGISTROS'] = lista_nueva


    return render_template(app.config['HTML_ADDAPITOKENUSER'], datos=datos)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA DE UN API TOKEN
@app.route('/apitokenadd/', methods=['GET', 'POST'])
def apitokenadd():

    # SI EL METOD ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        
        # Realizamos el insert el registro de api de registros
        errores = classRequest.requestAdd(app.config['TABLA_API_TOKEN'], **datos_dict)

        # Verifica si el add no fue exitosa
        if errores != True:

            # REDIRECCIONO A UNA PAGINA DE RESPUESTA
            return redirect(url_for('.respuesta'))

        # Si fue exitosa
        else:
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:
                return jsonify(formulario.apitokenaddhlp())

    # ENVIO LOS CAMPOS PARA EL FORMULARIO DE ALTA
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Recupera los cursores
    qry = 0
    id = 0
    # Recupera todos los api token users
    data_list_api_token_users, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TOKEN_USER'])

    # Recupera todos los registros
    data_list_api_registros, errores = classRequest.requestWrk(id, qry, app.config['TABLA_API_TOKEN_REGISTRO'])

    # Obtenemos el diccionario con la estructura para enviar al front-end
    datos = formulario.apitokenaddhlp()

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tratamiento de el select de api token user
    datos_slttokenuser = copy.deepcopy(datos['add']['SLTAPIUSER'][0])
    datos['add']['SLTAPIUSER'].clear()

    # Procesamos la lista de api token users
    lista_nueva = slt_comobobox(data_list_api_token_users, **datos_slttokenuser)
    datos['add']['SLTAPIUSER'] = lista_nueva

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tratamiento de el select de registros
    datos_sltregistros = copy.deepcopy(datos['add']['SLTAPIREGISTROS'][0])
    datos['add']['SLTAPIREGISTROS'].clear()

    # Procesamos la lista de los api de registros
    lista_nueva = slt_comobobox(data_list_api_registros, **datos_sltregistros)
    datos['add']['SLTAPIREGISTROS'] = lista_nueva

    return render_template(app.config['HTML_ADDAPITOKEN'], datos=datos)


#-------------------------------------------------------------------------
# ES LA RUTA PARA MODIFICAR UN TIPO DE DOCUMENTOS
@app.route('/provinciaupd/<int:id>', methods=['GET', 'POST'])
def provinciaupd(id):

    # SI EL METODO ES GET
    if request.method == 'GET':

        # Generamos el diccionario de busqueda
        datos_dict_get = {'clave': id}
        registros, error = classRequest.requestGet(app.config['TABLA_PROVINCIA'], **datos_dict_get)

        # Si no existe el id
        if len(registros) == 0:

            # Hacia donde se renderiza
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:

                # Retorna un json
                return jsonify(error)

            else:

                # Renderizo el Html
                return render_template(app.config['HTML_ERRNOEXISTE'], datos=error)

        # Si existe el id
        else:

            # Obtenemos el diccionario con la estructura para enviar al front-end
            lista_registro = [registros]
            return render_template(app.config['HTML_UPDPROVINCIAS'], datos=formulario.provinciaupdhlp(*lista_registro))

    
    # SI EL METODO ES POST
    if request.method == 'POST':

        # Obtenemos los datos del formulario
        datos       = request.form
        datos_dict  = datos.to_dict()

        # Generamos el diccionario de busqueda
        datos_dict_get = {'clave': id}
        registros, error = classRequest.requestGet(app.config['TABLA_PROVINCIA'], **datos_dict_get)

        # Si no existe el id
        if len(registros) == 0:

            # Hacia donde se renderiza
            if app.config['SWITCH_RENDER_TEMPLATE'] == False:

                # Retorna un json
                return jsonify(error)

            else:

                # Renderizo el Html
                return render_template(app.config['HTML_ERRNOEXISTE'], datos=error)

        # Si existe el id
        else:

            datos_dict = {'clave': id, 'datos': datos_dict}

            # Realizamos el update el registro de provincia
            errores = classRequest.requestUpd(app.config['TABLA_PROVINCIA'], **datos_dict)

            datos_dict_update = {'errores':errores, 'formato':formulario.provinciaupdhlp()}
            return render_update(app.config['HTML_UPDPROVINCIAS'], datos=datos_dict_update)











# -------------------------------------------------------------------------
# ES LA RUTA PARA VISUALIZAR LA RESPUESTA DEL FORMULARIO
# -------------------------------------------------------------------------
@app.route('/respuesta/')
def respuesta():

    return render_template('f#0001ok.html')



#-------------------------------------------------------------------------
# -- Esta sentencia me permite hacer un loop siempre escuchando
#-------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

