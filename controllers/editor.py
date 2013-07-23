# coding: utf-8
__author__ = 'Evolutiva'

def index():
    entity=request.args(0)
    id=request.args(1) or None
    alias=request.args(2)
    profile=alias
    imagen=None
    return dict(entity=entity,profile=profile,imagen=None,_id=id)

def search():
    from poderopedia import poderopedia
    entity=request.args(0)
    alias=request.args(1) or None

    result='Debe ingresar una búsqueda'
    if alias is not None:
        api = poderopedia(user_key=user_key)
        result = api.search(entity=entity,alias=alias)
    table=''
    key = 'person'
    if entity=='organizacion':
        key = 'organization'

    html = TABLE(TR(TH('ID'),TH('alias'),TH('bio')),
                [TR(TD(item['id']),TD(item['alias']),TD(item['shortBio'],
                TD(A('Seleccionar',_href=URL('editor','index',args=[entity,item['id']],extension=False))))) for item in result[key]])

    return dict(result=html)

@service.json
def get_connection():
    response.view='generic.json'
    from poderopedia import poderopedia
    entity=request.args(0)
    id=request.args(1) or None

    result='Debe ingresar una búsqueda'
    if id is not None:
        api = poderopedia(user_key=user_key)
        result = api.get_connections(entity=entity,id=id)

    return result


def childnodes():
    idx=request.args(0)
    json={}
    if idx[0]=='P':
        redirect(URL('editor','get_connection',args=['persona',int(idx[1:])]))
    elif idx[0]=='O':
        redirect(URL('editor','get_connection',args=['organizacion',int(idx[1:])]))
    return locals()