#! /usr/bin/env python3
# coding: utf-8

"""Module which defines all classes and functions related to the parser."""

import unidecode
import re


class Parser:
    def __init__(self, raw_data):
        self.text = raw_data

    def _text_to_lowercase(self):
        self.text = self.text.lower()

    def _remove_accents(self):
        self.text = unidecode.unidecode(self.text)

    def _remove_extra_spaces_between_words(self):
        self.text = " ".join(self.text.split())

    def _stripping_leading_and_trailing_spaces(self):
        self.text.strip(' ')

    def _extract_location(self):
        expression = r"(l'adresse.*du*e*s*|ou.*trouver*|ou est|ou se situe)"\
            r"(?P<location>[^,;:?!.]*)"
        result = re.search(expression, self.text)
        if result:
            self.text = result.group('location')
            self.text = self.text.strip(" ")

    def clean_input(self):
        self._text_to_lowercase()
        self._remove_accents()
        self._remove_extra_spaces_between_words()
        self._stripping_leading_and_trailing_spaces()
        self._extract_location()
