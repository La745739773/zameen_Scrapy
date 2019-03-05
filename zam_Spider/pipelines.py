# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZamSpiderPipeline(object):
    def process_item(self, item, spider):
        with open('output.csv','a',encoding='utf-8') as file:
            file.write(item['Title'].replace(',','') + ',' + item['Address'].replace(',','') + ',' + item['Latitude'].replace(',','') + ',' + item['Longitude'].replace(',','') +',' + item['Type'].replace(',','') + ',' + item['Price'].replace(',','') + ',' +
                       item['Location'].replace(',','') + ',' + item['Baths'].replace(',','') + ',' + item['Area'].replace(',','') + ',' + item['Purpose'].replace(',','') + ',' + item['Bedrooms'].replace(',','') + ',' + item['Added'].replace(',','') + '\n')
        return item
