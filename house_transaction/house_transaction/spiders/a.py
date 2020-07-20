# -*- coding: utf-8 -*-
import scrapy
import re
import base64
from fontTools.ttLib import TTFont
from scrapy.http import Request
from house_transaction.items import HouseItem




class ASpider(scrapy.Spider):
    name = 'a'
    allowed_domains = ['luzhou.58.com/chuzu']
    start_urls = ['http://luzhou.58.com/chuzu/']


    def parse(self, response):

        title_urls = response.css('div.des h2 a.strongbox::attr(href)').extract()

        res_html = response.text
        title = r'(?:target="_blank" |target="_blank"  rel="nofollow" )>(.*?)</a>'
        titles = re.findall(title, res_html, re.S | re.M)
        room = r'<p class="room">(.*?)</p>'
        rooms = re.findall(room, res_html, re.S | re.M)
        money = r'<b class="strongbox">(.*?)</b>'
        moneys = re.findall(money, res_html, re.S | re.M)

        # 处理信息
        titles = [c.replace('\n', '') for c in titles]
        titles = [c.replace(' ', '') for c in titles]
        rooms = [c.replace(' ', '') for c in rooms]
        rooms = [c.replace('&nbsp;', ' ') for c in rooms]

        sizes = []
        looks = []
        for i in range(0, len(rooms)):
            looks.append(rooms[i].split(" ", 1)[0])
            sizes.append(rooms[i].split(" ", 1)[1])
        sizes = [c.replace(' ', '') for c in sizes]
        sizes = [c.replace('\n', '') for c in sizes]


        font_pattern = r"base64,(.*?)format"
        font_base64 = re.findall(font_pattern, res_html, re.S | re.M)

        # 解码数字
        str_base64 = font_base64[0][:-3]
        bin_data = base64.decodebytes(str_base64.encode())
        with open("font.woff", r"wb") as f:
            f.write(bin_data)
        onlineFonts = TTFont('font.woff')
        self.dict = onlineFonts.getBestCmap()
        # 数字解决
        for i in range(len(titles)):
            titles[i] = self.convert_title_room(titles[i])
        for i in range(len(rooms)):
            looks[i] = self.convert_title_room(looks[i])
        for i in range(len(rooms)):
            sizes[i] = self.convert_title_room(sizes[i])
        for i in range(len(moneys)):
            moneys[i] = self.convert_money(moneys[i])

        house_item = HouseItem()
        house_item["title_urls"] = [title_urls]
        house_item["titles"] = [titles]
        house_item["moneys"] = [moneys]
        house_item["looks"] = [looks]
        house_item["sizes"] = [sizes]

        # 解析具体页
        for title_url in title_urls:
            yield Request(url=title_url, callback=self.parse_detail)


        # 下一页
        # next_urls = response.css('div.pager a.next::attr(href)').extract()
        # if next_urls:
        #     yield Request(url=next_urls, callback=self.parse)

        yield house_item


    def parse_detail(self, response):
        res_html = response.text
        url_title = r'class="c_333 f20 strongbox">(.*?)</h1>'
        url_title = re.findall(url_title, res_html, re.S | re.M)
        font_pattern = r"base64,(.*?)format"
        font_base64 = re.findall(font_pattern, res_html, re.S | re.M)
        # 解码数字
        str_base64 = font_base64[0][:-3]
        bin_data = base64.decodebytes(str_base64.encode())
        with open("font.woff", r"wb") as f:
            f.write(bin_data)
        onlineFonts = TTFont('font.woff')
        self.dict = onlineFonts.getBestCmap()
        # 数字解决
        url_title = self.convert_title_room(url_title[0])

        regions1 = response.css('a[onclick="clickLog(\'from=fcpc_detail_luzhou_quyu0\')"].c_333.ah::text').extract()
        regions2 = response.css('a[onclick="clickLog(\'from=fcpc_detail_luzhou_shangquan0\')"].c_333.ah::text').extract()
        figure_url = response.css('ul.house-pic-list li.pic img::attr(lazy_src)').extract()

        house_item_2 = HouseItem()
        house_item_2["url_title"] = [url_title]
        house_item_2["regions1"] = [regions1]
        house_item_2["regions2"] = [regions2]
        house_item_2["figure_url"] = [figure_url]

        yield house_item_2

    def convert_money(self, s):
        console = ''
        strs = {'&#x9476': 38006, '&#x958f': 38287, '&#x993c': 39228, '&#x9a4b': 39499, '&#x9e3a': 40506,
                '&#x9ea3': 40611, '&#x9f64': 40804, '&#x9f92': 40850, '&#x9fa4': 40868, '&#x9fa5': 40869}
        con_s = s.split(';')
        con_s = con_s[:-1]
        for i in con_s:
            temp = int(self.dict[strs[i]][-2:]) - 1
            console += str(temp)
        if console != '':
            return int(console)

    def convert_title_room(self, s):
        strs = ['&#x9476;', '&#x958f;', '&#x993c;', '&#x9a4b;', '&#x9e3a;', '&#x9ea3;', '&#x9f64;', '&#x9f92;',
                '&#x9fa4;', '&#x9fa5;']
        nums = {'&#x9476;': 38006, '&#x958f;': 38287, '&#x993c;': 39228, '&#x9a4b;': 39499, '&#x9e3a;': 40506,
                '&#x9ea3;': 40611, '&#x9f64;': 40804, '&#x9f92;': 40850, '&#x9fa4;': 40868, '&#x9fa5;': 40869}
        for str_c in strs:
            beg = s.find(str_c)
            if beg != -1:
                temp = str(int(self.dict[nums[str_c]][-2:]) - 1)
                s = s.replace(str_c, temp)
            else:
                continue
        return s

