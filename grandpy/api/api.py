#! /usr/bin/env python3
# coding: utf-8

"""Module which defines all classes and functions API related ."""

import requests
import json

from api.configapi import HERE_APP_ID, HERE_APP_CODE


class Here:

    def __init__(self, text_parsed):
        self.text_parsed = text_parsed
        self.error = False

    def _getting_raw_info_from_api_places(self):

        url = "https://places.cit.api.here.com/places/v1/discover/search"

        data = {
            "at": "48.8579,2.3437",
            "q": self.text_parsed,
            "Accept-Language": "fr-FR%2Cfr%3Bq%3D0.9%2Cen%3Bq%3D0.8",
            "app_id": HERE_APP_ID,
            "app_code": HERE_APP_CODE,
        }

        raw_result = requests.get(url, params=data)
        return raw_result.json()

    def _sorting_raw_info(self):
        try:
            # Reducing from the raw dict to the list we want to extact infos
            # #################################################################
            raw_result = self._getting_raw_info_from_api_places()
            items = raw_result['results']
            itemskey = items.get('items')
        except ValueError:
            self.error = True
        except IndexError:
            self.error = True
        except TypeError:
            self.error = True
        except KeyError:
            self.error = True

        return itemskey

    def _from_sorted_raw_info_to_location_name(self):
        itemskey = self._sorting_raw_info()
        # Assign the name of the location returned
        title = itemskey[0].get('title')
        return title

    def _from_sorted_raw_info_to_location_position(self):
        itemskey = self._sorting_raw_info()
        # Assign the position of the result returned
        position = itemskey[0].get('position')
        return position

    def _from_sorted_raw_info_to_location_link(self):
        itemskey = self._sorting_raw_info()
        # Assign the link raw data (containing a link to a map, the address
        # , the website link if available, phone number if available, etc.)
        # of the result returned
        href = itemskey[0].get('href')
        return href

    def getting_sorted_informations(self):
        # Assign the differents informations to variables
        # #################################################################
        sorted_info = [
            self._from_sorted_raw_info_to_location_name(),
            self._from_sorted_raw_info_to_location_position(),
            self._from_sorted_raw_info_to_location_link()
        ]
        return sorted_info


class Wiki:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def _getting_raw_info_from_api_geosearch(self):
        url = "https://fr.wikipedia.org/w/api.php"

        data = {
            "action": "query",
            "list": "geosearch",
            "format": "json",
            "gsradius": 10000,
            "gscoord": str(self.latitude) + "|" + str(self.longitude)
        }

        raw_result = requests.get(url, params=data)
        return raw_result.json()

    def _from_sorted_raw_info_to_article_id(self):
        raw_result = self._getting_raw_info_from_api_geosearch()
        pageid = raw_result["query"]["geosearch"][0]["pageid"]
        return pageid

    def _getting_raw_info_from_api_extract(self):
        url = "https://fr.wikipedia.org/w/api.php"

        data = {
            "action": "query",
            "prop": "extracts" + "|" + "info",
            "inprop": "url",
            "exchars": 300,
            "pageids": self._from_sorted_raw_info_to_article_id(),
            "format": "json",
            "explaintext": ""
        }

        raw_result = requests.get(url, params=data)
        return raw_result.json()

    def getting_extract_from_closest_wiki_page(self):
        raw_result = self._getting_raw_info_from_api_extract()
        page_id = self._from_sorted_raw_info_to_article_id()
        extract = raw_result["query"]["pages"][str(page_id)]["extract"]
        return extract

    def getting_url_from_closest_wiki_page(self):
        raw_result = self._getting_raw_info_from_api_extract()
        page_id = self._from_sorted_raw_info_to_article_id()
        url = raw_result["query"]["pages"][str(page_id)]["fullurl"]
        return url
    

# ##########Test##############
instance_wiki = Wiki(37.786971, -122.399677)

print(instance_wiki.getting_url_from_closest_wiki_page())
# ############################.