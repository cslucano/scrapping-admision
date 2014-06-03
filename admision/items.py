# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class IngresanteItem(Item):
    # define the fields for your item here like:
    codigo = Field()
    nombres = Field()
    p1 = Field()
    p2 = Field()
    p3 = Field()
    acumulado = Field()
    vocacional = Field()
    cne = Field()
    arq  = Field()
    final = Field()
    ingreso  = Field()
    merito_modalidad  = Field()
    modalidad_ingreso  = Field()
    especialidad_ingreso  = Field()
    obs  = Field()
