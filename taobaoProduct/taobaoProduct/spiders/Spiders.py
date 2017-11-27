#coding:utf-8



from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
import json
from taobaoProduct.items import TaobaoproductItem



# https://s.taobao.com/search?q=python
class taobao(BaseSpider):
	name = 'taobao'
	allowed_domains = ['s.taobao.com']
	# start_urls = ['https://s.taobao.com/search?q=python']



	def start_requests(self):
		# https://s.taobao.com/search?data-key=s&data-value=0&ajax=true&_ksTS=1511765682474_1574&callback=jsonp1575&q=python&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=0
		print '---------------先走哪一步---------------'
		

		for i in range(10):
			data_value = i * 44
			if i == 0:
				s = 0
			else:
				s = (i - 1)* 44

			jsonUrl = 'https://s.taobao.com/search?data-key=s&data-value=%s&ajax=true&_ksTS=1511765682474_1574&callback=jsonp1575&q=python&bcoffset=4&ntoffset=4&p4ppushleft=1,48&s=%s'%(data_value,s)
			print jsonUrl
			yield Request(jsonUrl,self.parse_json)
		# pass
	def parse_json(self, response):
		print '+++++++++++++成功进来了++++++++++++++'
		with open('json.html','wb') as f:
			f.write(response.body[12:-2])
		result = json.loads(response.body[12:-2])

		item_list = result['mods']['itemlist']['data']['auctions']

		item = TaobaoproductItem()


		print '+++++++++++++++++打印title+++++++++++++++++++++++'+ str(len(item_list))
		for it in item_list:
			item['nid'] = it['nid']
			item['title'] = it['title']
			item['raw_title'] = it['raw_title']
			item['detail_url'] = it['detail_url']
			item['view_price'] = it['view_price']
			item['view_fee'] = it['view_fee']
			item['item_loc'] = it['item_loc']
			item['view_sales'] = it['view_sales']
			item['comment_count'] = it['comment_count']
			item['user_id'] = it['user_id']
			item['nick'] = it['nick']
			item['comment_url'] = it['comment_url']
			item['shopLink'] = it['shopLink']
			yield item
		print '+++++++++++++++++打印title结束+++++++++++++++++++++++'
		

		



	# def parse(self, response):
	# 	print '===========中文中文中文中文中文中文============'
	# 	with open('taobao.html','wb') as f:
	# 		f.write(response.body)

	# 	hxp = Selector(response)
	# 	item_list = hxp.select("//div[@class='m-itemlist']//div[@class='items']/div[@class='J_MouserOnverReq']/@data-index").extract()
		
	# 	print '***********开始爬取数据***************'
	# 	for inde in item_list:
	# 		print inde
	# 	print '***********爬取数据结束***************'



