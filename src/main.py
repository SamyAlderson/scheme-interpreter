"""
Fichier principal de l'interpréteur Scheme.
Charge les fichiers Scheme et les exécute.
"""

import sys
import importlib
from src.scheme import SchemeInterpreter

def charger_fichier_schemefichier(fichier):
    """
    Charge un fichier Scheme et l'exécute.

    Args:
        fichier (str): Chemin du fichier Scheme à charger.

    Raises:
        ValueError: Si le fichier n'est pas trouvé ou si la syntaxe est invalide.
    """
    try:
        with open(fichier, 'r') as f:
            code = f.read()
            interpreter = SchemeInterpreter(code)
            interpreter.executer()
    except FileNotFoundError as e:
        print(f"Erreur: Fichier {fichier} non trouvé.")
        raise
    except Exception as e:
        print(f"Erreur: {e}")
        raise

def charger_fichier_scheme(fichiers):
    """
    Charge les fichiers Scheme et les exécute.

    Args:
        fichiers (list[str]): Liste de chemins des fichiers Scheme à charger.

    Raises:
        ValueError: Si un fichier n'est pas trouvé ou si la syntaxe est invalide.
    """
    for fichier in fichiers:
        charger_fichier_schemefichier(fichier)

def main():
    """
    Programme principal de l'interpréteur Scheme.
    """
    if len(sys.argv) != 2:
        print("Erreur: S'il vous plaît spécifiez le ou les fichiers Scheme à charger.")
        return

    fichiers = sys.argv[1].split(',')
    charger_fichier_scheme(fichiers)

if __name__ == "__main__":
    main()
```

```python
"""
Module SchemeInterpreter.
Implémentation de l'interpréteur Scheme.
"""

class SchemeInterpreter:
    """
    Interpréteur Scheme.
    """

    def __init__(self, code):
        """
        Constructeur de l'interpréteur.

        Args:
            code (str): Code Scheme à exécuter.
        """
        self.code = code

    def executer(self):
        """
        Exécute le code Scheme.
        """
        # Implémentation de l'exécution du code Scheme
        pass