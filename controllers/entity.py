#coding: utf-8
__author__ = 'Evolutiva'

def new():
    form=FORM(XML('<b>Búsqueda Perfil</b>'),BR(),
              SELECT('Seleccione Entidad ->','persona', 'organizacion',_name='entity'),BR(),
              'Nombre:',INPUT(_label='nombre',_name='alias'), BR(),INPUT(_type='submit')
    )

    if form.validate():
        redirect(URL('editor','search',args=[form.vars.entity,form.vars.alias]))

    return dict(form=form)