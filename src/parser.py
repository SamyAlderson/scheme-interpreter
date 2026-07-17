"""
Module pour la compilation des jetons en abstrait syntaxique
"""

import ast
from typing import List

class Parser:
    """
    Classe pour la compilation des jetons en abstrait syntaxique
    """

    def __init__(self, tokens: List[str]):
        """
        Initialisation du parser avec une liste de jetons

        Args:
            tokens (List[str]): Liste de jetons à compiler
        """
        self.tokens = tokens

    def parse(self) -> ast.AST:
        """
        Compile les jetons en abstrait syntaxique

        Returns:
            ast.AST: Représentation abstraite du code Scheme
        """
        try:
            return ast.parse(self.tokens)
        except SyntaxError as e:
            raise ValueError(f"Erreur de syntaxe : {e}")

    def get_tokens(self) -> List[str]:
        """
        Récupère la liste des jetons

        Returns:
            List[str]: Liste des jetons
        """
        return self.tokens

class TokenError(Exception):
    """
    Classe d'erreur pour les problèmes de jetons
    """

class SyntaxError(Exception):
    """
    Classe d'erreur pour les problèmes de syntaxe
    """
```

```python
# Exemple d'utilisation du parser
if __name__ == "__main__":
    tokens = ["def", "add", "(", "x", "+", "y", ")", "{", "return", "x", "+", "y", "}"]
    parser = Parser(tokens)
    parsed_tree = parser.parse()
    print(parsed_tree)