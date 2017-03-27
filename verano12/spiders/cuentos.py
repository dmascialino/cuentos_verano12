# -*- coding: utf-8 -*-

import datetime

import scrapy


class CuentosSpider(scrapy.Spider):
    name = "cuentos"
    allowed_domains = ["pagina12.com.ar"]

    def start_requests(self):
        BASE_URL = 'https://www.pagina12.com.ar/suplementos/verano12/notas?date={}'
        d = datetime.date(2016, 12, 27)
        while d <= datetime.date(2017, 3, 4):
            meta = {'date': d}
            url = BASE_URL.format(d.strftime('%Y-%m-%d'))
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
            d += datetime.timedelta(days=1)

    def parse(self, response):
        selector = response.css("div.article-box__container a ::attr(href)")
        meta = response.meta
        if len(selector) != 2:
            self.logger.error("slector != 2. %s", response.url)
            yield None
        else:
            links = {s.extract() for s in selector}
            link_autor = next(l for l in links if l.endswith('el-cuento-por-su-autor'))
            links.discard(link_autor)
            link = links.pop()
            meta['link_autor'] = link_autor
            yield scrapy.Request(link, callback=self.parse_cuento, meta=meta)

    def parse_cuento(self, response):
        meta = response.meta
        titulo = response.css("div.article-title ::text").extract_first().strip()
        autor_cuento = response.css("div.article-author a ::text").extract_first().strip()
        imagen_cuento = response.css("div.article-main-media-image "
                                     "img.show-for-large ::attr(data-src)").extract_first()
        texto_cuento = response.css("div.article-text ::text").extract()
        link_autor = response.meta['link_autor']
        if link_autor is None:
            self.logger.error("link_autor is None")
            yield None

        meta.update({"titulo": titulo,
                     "autor_cuento": autor_cuento,
                     "imagen_cuento": imagen_cuento,
                     "texto_cuento": texto_cuento})
        yield scrapy.Request(link_autor, callback=self.parse_autor, meta=meta)

    def parse_autor(self, response):
        meta = response.meta
        meta['imagen_autor'] = response.css("div.article-main-media-image "
                                            "img.show-for-large ::attr(data-src)").extract_first()
        meta['texto_autor'] = response.css("div.article-text ::text").extract()
        yield meta
