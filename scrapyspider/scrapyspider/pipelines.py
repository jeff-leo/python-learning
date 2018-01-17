# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanPipeline(object):
    # 这个名称的电影不输出
    words_to_filter = ['肖申克的救赎']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word == item['movie_name']:
                raise TypeError
        return item
