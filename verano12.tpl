=============
Verano12 2017
=============

:creator: Diego Mascialino
:publisher: Diego Mascialino
:title: Cuentos Verano12, 2017
:description: Recopilcacion de cuentos publicados en Pagina/12
:language: Spanish
:subject: Cuentos
:rights: Copyright -- Pagina/12 -- All rights reserved

.. titlepage

.. The above comment indicates that this will be a titlepage

.. You can include HTML if you want

.. raw:: html

  <div class="Title">
  <h1 class="center">Cuentos Verano12</h1>
  </div>

{% for cuento in cuentos %}
{{ cuento.titulo }}

.. container:: imagewrapperhi

    .. image:: {{ cuento.img_autor }}

{{ cuento.texto_cuento }}


El cuento por su autor
----------------------

.. image:: {{ cuento.img_cuento }}

{{ cuento.texto_autor }}



.. raw:: html

    <div style="page-break-before:always;"></div>


{% endfor %}
