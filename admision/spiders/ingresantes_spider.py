from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from admision.items import IngresanteItem

class IngresantesSpider(Spider):
    name = "ingresantes"
    allowed_domains = ["admision.uni.edu.pe"]
    start_urls = [
        "http://www.admision.uni.edu.pe/resultado_adm.php"
    ]

    def parse(self, response):
        base_url = response.url
        paginas = range(1,271)
        for pagina in paginas:
           url = '%s?pagina=%s' % (base_url, pagina)
           yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        sel = Selector(response)
        codigos = sel.xpath('/html/body/table/tr/td[2]/div/table/tr[2]/td/table/tr/td/table/tr/td/table[3]/tr[position()>1]')
        items = []
        for codigo in codigos:
            item = IngresanteItem()
            item['codigo'] = codigo.xpath('td[2]/text()').extract()
            item['nombres'] = codigo.xpath('td[3]/text()').extract()
            item['p1'] = codigo.xpath('td[4]/text()').extract()
            item['p2'] = codigo.xpath('td[5]/text()').extract()
            item['p3'] = codigo.xpath('td[6]/text()').extract()
            item['acumulado'] = codigo.xpath('td[7]/text()').extract()
            item['vocacional'] = codigo.xpath('td[8]/text()').extract()
            item['cne'] = codigo.xpath('td[9]/text()').extract()
            item['arq'] = codigo.xpath('td[10]/text()').extract()
            item['final'] = codigo.xpath('td[11]/text()').extract()
            item['ingreso'] = codigo.xpath('td[12]/text()').extract()
            item['merito_modalidad'] = codigo.xpath('td[13]/text()').extract()
            item['modalidad_ingreso'] = codigo.xpath('td[14]/text()').extract()
            item['especialidad_ingreso'] = codigo.xpath('td[15]/text()').extract()
            item['obs'] = codigo.xpath('td[16]/text()').extract()
            items.append(item)
        return items
