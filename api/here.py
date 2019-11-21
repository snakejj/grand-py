#! /usr/bin/env python3
# coding: utf-8

"""Module which defines all classes and functions related to the HERE's API."""

import requests
import json

from configapi import HERE_APP_ID, HERE_APP_CODE


class Here:

    def __init__(self, text_parsed):
        self.text_parsed = text_parsed

    def getting_raw_info_from_api_places(self):

        url = "https://places.cit.api.here.com/places/v1/discover/search"

        data = {
            "at": "48.8579,2.3437",
            "q": self.text_parsed,
            "Accept-Language": "fr-FR%2Cfr%3Bq%3D0.9%2Cen%3Bq%3D0.8",
            "app_id": HERE_APP_ID,
            "app_code": HERE_APP_CODE,
        }

        response = requests.get(url, params=data)
        print(response)
        result = json.loads(response.text)
        print(result)

    def sorting_raw_info(self):
        pass


# ##########Test##############
instancedehere = Here("La defense")
instancedehere.getting_raw_info_from_api_places()
# ############################
