# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChampionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    win_rate = scrapy.Field()
    play_rate = scrapy.Field()
    ban_rate = scrapy.Field()
    avg_played = scrapy.Field()
    gold_earned = scrapy.Field()
    kills = scrapy.Field()
    deaths = scrapy.Field()
    assists = scrapy.Field()
    dmg_dealt = scrapy.Field()
    dmg_taken = scrapy.Field()
    minions_killed = scrapy.Field()


class RoleItem(scrapy.Item):

    # first highest percentage role
    role_1 = scrapy.Field()
    percent_played_1 = scrapy.Field()
    games_played_1 = scrapy.Field()

    # second highest percentage role
    role_2 = scrapy.Field()
    percent_played_2 = scrapy.Field()
    games_played_2 = scrapy.Field()

    # jungle role
    role_jungle = scrapy.Field()
    percent_played_jungle = scrapy.Field()
    games_played_jungle = scrapy.Field(


class DataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

class PatchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
