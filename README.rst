Descripción
===========

Proyecto para descargar recopilación de cuentos publicados en Pagina12.
Convertirlos a restructured text, luego usando rst2epub2 se puede obtener un epub.

Los comandos para utilizarlo::

  scrapy crawl cuentos -o cuentos.json -L INFO
  python items_to_rst.py
  PYTHONPATH=../rst2epub2-master python ../rst2epub2-master/rst2epub.py verano12.rst verano12.epub --traceback --stylesheet verano12.css

Este proyecto fue realizado durante el PyCamp 2017, organizado por PyAr.

Autores
=======
- Mario Chacon <the.masch@gmail.com>
- Laureano Silva <laureano.bara@gmail.com>
- Diego <dmascialino@gmail.com>

Nota
====

En `rst2epub2` hay un bug al tener unicode en el índice (que se realiza con el título de los cuentos). 
Si se obtiene el error::

  UnicodeEncodeError: 'ascii' codec can't encode character ...

  The specified output encoding (utf-8) cannot
  handle all of the output.
  Try setting "--output-encoding-error-handler" to

  * "xmlcharrefreplace" (for HTML & XML output);
    the output will contain "&#237;" and should be usable.
  * "backslashreplace" (for other output formats);
    look for "\xed" in the output.
  * "replace"; look for "?" in the output.

  "--output-encoding-error-handler" is currently set to "xmlcharrefreplace".


Se puede solucionar, editando `rst2epub2-master/epublib/epub.py` y reemplazando la función `_write_toc_ncx`, con:

.. code:: diff

    def _write_toc_ncx(self):
        self.toc_map_root.assign_play_order()
        fout = open(os.path.join(self.root_dir, 'OEBPS', 'toc.ncx'), 'wb')
        tmpl = self.loader.load('toc.ncx')
        stream = tmpl.generate(book=self)
        fout.write(stream.render('xml').encode('utf-8'))
        fout.close()
