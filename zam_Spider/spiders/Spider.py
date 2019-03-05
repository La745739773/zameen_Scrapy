import scrapy 
import time
from zam_Spider.items import ZamSpiderItem

city_name = ''
city_code = ''
class zam_Spider(scrapy.Spider):
    name = 'zam'

    totalNumber = 0
    Allhouseurl_List = []
    def start_requests(self):
        city_name = input('Please input the city name: ') #Faisalabad
        city_code = input('Please input the city code: ')
        totalNumber = int(input('Please input the number of houseInfo: '))
        page_url = ['https://www.zameen.com/Homes/' + city_name + '-' + city_code + '-1' + '.html']
        if int(totalNumber / 25) > 50:
            for i in range(50,int(totalNumber / 25) + 1):
                page_url.append('https://www.zameen.com/Homes/' + city_name + '-' + city_code + '-' + str(i) + '.html')
        for url in page_url:
            yield scrapy.Request(url=url, callback=self.parse) #爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        houseUrl_List = response.xpath("//a[@class='_7ac32433']/@href").extract()
        for url in houseUrl_List:
            try:
                yield scrapy.Request(url = 'https://www.zameen.com' + url, callback=self.Parse_HouseInfo)
            except IOError:
                continue
        nextpage_url = response.xpath("//a[@title='Next']/@href").extract()
        print('https://www.zameen.com'+ nextpage_url[0])
        yield scrapy.Request(url='https://www.zameen.com' + nextpage_url[0], callback=self.parse)

    def Parse_HouseInfo(self, response): #爬取 地址、Details、Lng and Lat
        item = ZamSpiderItem()
        item['Title'] = response.xpath("//h1[@class='_64bb5b3b']/text()").extract()[0].strip()
        item['Address']= response.xpath("//div[@class='cbcd1b2b']/text()").extract()[0].strip()
        #item['Details'] = response.xpath("//div[@class='_141f596c']/div/ul/li").extract()
        Details_content = response.xpath("//div[@class='_141f596c']/div//ul/li")
        item['Type'] = Details_content[0].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        item['Price'] = Details_content[1].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip() + ' ' + Details_content[1].xpath(".//span[@class='_812aa185']/text()").extract()[-1].strip()
        item['Location'] = Details_content[2].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        item['Baths'] = Details_content[3].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        item['Area'] = Details_content[4].xpath(".//span[@class='_812aa185']/span/text()").extract()[0].strip()
        item['Purpose'] = Details_content[5].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        item['Bedrooms'] = Details_content[6].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        item['Added'] = Details_content[7].xpath(".//span[@class='_812aa185']/text()").extract()[0].strip()
        Lat_index = response.text.find('latitude')
        item['Latitude'] = response.text[Lat_index+10:Lat_index+19]
        Lng_index = response.text.find('longitude')
        item['Longitude'] = response.text[Lng_index + 11 :Lng_index + 20]
        #print(item)

        yield item