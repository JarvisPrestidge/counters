import scrapy
import requests
import re


class CountersSpider(scrapy.Spider):

    def __init__(self):
        base_url = "http://champion.gg/champion/"
        # query riot static data api for champions list
        r = requests.get("https://global.api.pvp.net/api/lol/static-data/"
                         "euw/v1.2/champion?api_key=81962b95-cdc4-42de-bb2"
                         "8-9c8a6736aeaa")
        r.encoding = 'UTF-8'
        data = r.json()
        # list of champion names (with Wukong as MonkeyKing)
        champs = ["MonkeyKing" if data['data'].values()[x]['name'] == "Wukong"
                  else data['data'].values()[x]['name']
                  for x in range(len(data['data']))]
        # regex to remove all non-alpha
        non_alpha = re.compile('[^a-zA-Z]')
        # create individual champ urls
        self.start_urls = [
            ("%s%s" % (base_url, non_alpha.sub("", x))) for x in champs]

    name = "counters"
    allowed_domains = ['champion.gg']

    def parse(self, response):
        # get champion data
        champion = response.xpath(
            "/html/body/div[1]/div/div[3]/script[1]/text()").re(
            r"(?:matchupData\.champion.?=.?)(\{[^;]*)")[0]
        # get general role data
        role = response.xpath(
            "/html/body/div[1]/div/div[3]/script[1]/text()").re(
            r"(?:matchupData\.generalRole.?=.?)(\{[^;]*)")[0]
        # get big data
        data = response.xpath(
            "/html/body/div[1]/div/div[3]/script[1]/text()").re(
            r"(?:matchupData\.championData.?=.?)(\{[^;]*)")[0]
        # get patch data
        patch = response.xpath(
            "/html/body/div[1]/div/div[3]/script[1]/text()").re(
            r"(?:matchupData\.patchHistory.?=.?)(\[[^;]*)")[0]
