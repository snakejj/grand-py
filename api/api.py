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


# ##########Test##############
instance_here = Here('la tour eiffel')

print(instance_here.getting_sorted_informations())
# ############################
