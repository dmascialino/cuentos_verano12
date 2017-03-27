
import datetime
import logging
import json
import os
import shutil

import jinja2

import requests

logging.basicConfig()


DATE_FORMAT = "%Y-%m-%d"


def datetime_parser(dct):
    for k, v in dct.items():
        if isinstance(v, basestring):
            try:
                dct[k] = datetime.datetime.strptime(v, DATE_FORMAT)
                print('aja')
            except:
                pass
    return dct


def download_image(url):
    logging.debug('Downloading %s', url)
    fname = 'imgs/' + url.rsplit('/', 1)[1].split('?')[0]

    if os.path.exists(fname):
        return fname

    response = requests.get(url, stream=True)
    if response.ok:
        with open(fname, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)


def subrayar(titulo, c='='):
    return titulo + '\n' + c*len(titulo)


def process(cuento):
    cuento['img_cuento'] = download_image(cuento['imagen_cuento'])
    cuento['img_autor'] = download_image(cuento['imagen_autor'])
    cuento['texto_cuento'] = ''.join(cuento['texto_cuento'])
    cuento['texto_autor'] = ''.join(cuento['texto_autor'])
    # cuento['titulo'] = subrayar(cuento['titulo'].strip().encode('ascii', 'replace'))
    print(type(cuento['date']), repr(cuento['date']))
    titulo = u'{titulo}, {autor_cuento}. {date:%d/%m/%y}'.format(**cuento)
    cuento['titulo'] = subrayar(titulo)
    return cuento


cuentos = json.load(open('cuentos.json'), object_hook=datetime_parser)

cuentos = [process(c) for c in cuentos]

cuentos = sorted(cuentos, key=lambda x: x['date'])
tpl = jinja2.Template(open('./verano12.tpl').read())

restructured = tpl.render(cuentos=cuentos)
with open('./verano12.rst', 'w') as fh:
    fh.write(restructured.encode('utf-8'))
