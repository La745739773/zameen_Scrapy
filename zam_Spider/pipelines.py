# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZamSpiderPipeline(object):
    def process_item(self, item, spider):
        with open('output.csv','a',encoding='utf-8') as file:
            file.write(item['Title'] + ',' + item['Address'] + ',' + item['Latitude'] + ',' + item['Longitude'] +',' + item['Type'] + ',' + item['Price'] + ',' +
                       item['Location'] + ',' + item['Baths'] + ',' + item['Area'] + ',' + item['Purpose'] + ',' + item['Bedrooms'] + ',' + item['Added'] + '\n')
        return item
