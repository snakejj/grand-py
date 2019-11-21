#! /usr/bin/env python3
# coding: utf-8

from parser import Parser


class TestParser:

    def test_parser_remove_capital_letters(self):
        sentence_test = "Texte Avec Des Majuscules A Transformer En Minuscule"
        parser = Parser(sentence_test)
        parser.clean()

        assert "T" not in parser.text
        assert "A" not in parser.text
        assert "D" not in parser.text
        assert "M" not in parser.text
        assert "E" not in parser.text

    def test_parser_remove_accents(self):
        sentence_test = "à é î ö ù è"
        parser = Parser(sentence_test)
        parser.clean()

        assert "à" not in parser.text
        assert "é" not in parser.text
        assert "î" not in parser.text
        assert "ö" not in parser.text
        assert "ù" not in parser.text
        assert "è" not in parser.text

    def test_parser_remove_extra_space(self):
        sentence_test = "one test  extra   space    beetween     words"
        parser = Parser(sentence_test)
        parser.clean()

        assert "  " not in parser.text
        assert "   " not in parser.text
        assert "    " not in parser.text
        assert "     " not in parser.text

    def test_parser_remove_spaces_in_beggining_and_the_end(self):
        sentence_test = " a b "
        parser = Parser(sentence_test)
        parser.clean()

        assert parser.text == "a b"

    def test_parser_extract_location_from_a_question(self):
        sentence_test = "ou se situe la tour montparnasse ?"
        parser = Parser(sentence_test)
        parser.clean()

        assert parser.text == "la tour montparnasse"
