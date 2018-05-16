# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urlencode
import json
from images360.items import Images360Item

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']
    
#Debug或许从一开始就没调用start_request
#its start_requests not start_request, there is more 's'.
    def start_requests(self):
        data = {'ch':'beauty','listtype':'new'}
        base_url = 'http://images.so.com/zj?'
        #num = self.settings.get('MAX_PAGE')+1
        #print(num)
        for page in range(1,2):#self.settings.get('MAX_PAGE')+1
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            #print(url)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        
        for image in result.get('list'):
            item = Images360Item()
            item['ids'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
            #print(item['ids'])

# =============================================================================
#     name = 'images'
#     allowed_domains = ['images.so.com']
#     start_urls = ['http://images.so.com/']
#     
#     
#     def start_requests(self):
#         data = {'ch': 'photography', 'listtype': 'new'}
#         base_url = 'https://images.so.com/zj?'
#         for page in range(1, self.settings.get('MAX_PAGE') + 1):
#             data['sn'] = page * 30
#             params = urlencode(data)
#             url = base_url + params
#             yield Request(url, self.parse)
#     
#     def parse(self, response):
#         result = json.loads(response.text)
#         for image in result.get('list'):
#             item = ImageItem()
#             item['id'] = image.get('imageid')
#             item['url'] = image.get('qhimg_url')
#             item['title'] = image.get('group_title')
#             item['thumb'] = image.get('qhimg_thumb_url')
#             yield item
# =============================================================================
