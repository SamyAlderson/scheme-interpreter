# tests/test_parser.py

"""
Fichiers de test pour le parser
"""

import unittest
from unittest.mock import Mock
from src.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_expression(self):
        """
        Test de la fonction parse_expression pour une expression simple
        """
        tokens = [
            {"type": "LITERAL", "value": "5"},
            {"type": "OPERATOR", "value": "+"},
            {"type": "LITERAL", "value": "3"}
        ]
        expected_result = {"type": "EXPRESSION", "value": "(+ 5 3)"}
        self.assertEqual(self.parser.parse_expression(tokens), expected_result)

    def test_parse_expression_with_error(self):
        """
        Test de la fonction parse_expression pour une expression avec une erreur
        """
        tokens = [
            {"type": "LITERAL", "value": "5"},
            {"type": "OPERATOR", "value": "+"},
            {"type": "SYMBOL", "value": "non-existent-variable"}
        ]
        with self.assertRaises(ValueError):
            self.parser.parse_expression(tokens)

    def test_parse_statement(self):
        """
        Test de la fonction parse_statement pour une déclaration simple
        """
        tokens = [
            {"type": "SYMBOL", "value": "x"},
            {"type": "ASSIGNMENT", "value": "="},
            {"type": "LITERAL", "value": "5"}
        ]
        expected_result = {"type": "STATEMENT", "value": "(define x 5)"}
        self.assertEqual(self.parser.parse_statement(tokens), expected_result)

    def test_parse_statement_with_error(self):
        """
        Test de la fonction parse_statement pour une déclaration avec une erreur
        """
        tokens = [
            {"type": "SYMBOL", "value": "x"},
            {"type": "ASSIGNMENT", "value": "="},
            {"type": "SYMBOL", "value": "non-existent-variable"}
        ]
        with self.assertRaises(ValueError):
            self.parser.parse_statement(tokens)

    def test_parse_program(self):
        """
        Test de la fonction parse_program pour un programme simple
        """
        tokens = [
            {"type": "LITERAL", "value": "5"},
            {"type": "OPERATOR", "value": "+"},
            {"type": "LITERAL", "value": "3"}
        ]
        expected_result = {"type": "PROGRAM", "value": "(+ 5 3)"}
        self.assertEqual(self.parser.parse_program(tokens), expected_result)

    def test_parse_program_with_error(self):
        """
        Test de la fonction parse_program pour un programme avec une erreur
        """
        tokens = [
            {"type": "LITERAL", "value": "5"},
            {"type": "OPERATOR", "value": "+"},
            {"type": "SYMBOL", "value": "non-existent-variable"}
        ]
        with self.assertRaises(ValueError):
            self.parser.parse_program(tokens)

if __name__ == '__main__':
    unittest.main()