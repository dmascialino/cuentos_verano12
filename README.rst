
Proyecto para descargar recopilación de cuentos publicados en Pagina12.

Convertirlos a restructured text, luego usando rst2epub2 se puede obtener un epub.

scrapy crawl cuentos -o cuentos.json -L INFO
python items_to_rst.py
PYTHONPATH=../rst2epub2-master python ../rst2epub2-master/rst2epub.py verano12.rst verano12.epub --traceback --stylesheet verano12.css


Este proyecto fue realizado durante el PyCamp 2017, organizado por PyAr.

Participaron:
- Mario Chacon <the.masch@gmail.com>
- Laureano Silva <laureano.bara@gmail.com>
- Diego <dmascialino@gmail.com>
