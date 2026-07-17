"""
Module pour le traitement du code Scheme en jetons

Le tokenizer est responsable de la lecture du code Scheme et de la conversion en jetons.
Chaque jeton est représenté par une valeur unique et un type spécifique.
Les types de jetons possibles sont :
- LIT_SYMB (symbole littéral)
- LIT_NUM (nombre littéral)
- LIT_STR (chaîne de caractères littérale)
- LIT_FONC (appel de fonction)
- LIT_OP (opérateur)
- LIT_VAR (variable)
- LIT_LIST (liste)
- LIT_ATOM (atome)
- FIN_LIST (fin de liste)
- FIN_ATOM (fin d'atome)
- FIN_EXPR (fin d'expression)

Les jetons sont stockés dans une liste de tuples, où le premier élément du tuple est le type de jeton
et le deuxième élément est la valeur du jeton.

:author: [Votre Nom]
:version: 1.0
:date: [Date]
"""

import re

from enum import Enum

class TokenType(Enum):
    """
    Enumération des types de jetons possibles
    """
    LIT_SYMB = 1
    LIT_NUM = 2
    LIT_STR = 3
    LIT_FONC = 4
    LIT_OP = 5
    LIT_VAR = 6
    LIT_LIST = 7
    LIT_ATOM = 8
    FIN_LIST = 9
    FIN_ATOM = 10
    FIN_EXPR = 11

class Token:
    """
    Classe représentant un jeton
    """
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Tokenizer:
    """
    Classe pour le traitement du code Scheme en jetons
    """
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []

    def tokenize(self):
        """
        Méthode pour la conversion du code Scheme en jetons
        """
        while self.pos < len(self.code):
            match = self.match()
            if match:
                self.tokens.append(Token(match[0], match[1]))
            else:
                raise ValueError("Erreur de syntaxe")

        return self.tokens

    def match(self):
        """
        Méthode pour la recherche d'un motif de jeton dans le code Scheme
        """
        for pattern, type in [
            (r"\d+", TokenType.LIT_NUM),
            (r"\"[^\"]*\"", TokenType.LIT_STR),
            (r"[a-zA-Z_][a-zA-Z_0-9]*", TokenType.LIT_SYMB),
            (r"\(", TokenType.LIT_FONC),
            (r"\)", TokenType.FIN_EXPR),
            (r"\.", TokenType.LIT_OP),
            (r",", TokenType.LIT_OP),
            (r"\[", TokenType.LIT_LIST),
            (r"\]", TokenType.FIN_LIST),
            (r"\{", TokenType.LIT_ATOM),
            (r"\}", TokenType.FIN_ATOM)
        ]:
            match = re.match(pattern, self.code[self.pos:])
            if match:
                self.pos += match.end()
                return (type, match.group())

        return None