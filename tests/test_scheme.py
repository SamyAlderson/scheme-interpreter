import unittest
from src.scheme import SchemeInterpreter, SchemeError
from src.tokenizer import SchemeTokenizer
from src.parser import SchemeParser
from src.main import execute_scheme

class TestSchemeInterpreter(unittest.TestCase):
    """Classe de tests pour l'interpréteur Scheme"""

    def test_execute_scheme(self):
        """Test l'exécution d'un programme Scheme"""
        code_scheme = "(define x 5)\n(define y (+ x 3))\n(display y)"
        tokens = SchemeTokenizer.tokenize(code_scheme)
        ast = SchemeParser.parse(tokens)
        try:
            scheme_interpreter = SchemeInterpreter(ast)
            result = scheme_interpreter.execute()
            self.assertEqual(result, "8")
        except SchemeError as e:
            self.fail(f"Erreur lors de l'exécution du code Scheme : {e}")

    def test_execute_scheme_error(self):
        """Test l'exécution d'un programme Scheme avec une erreur"""
        code_scheme = "(define x 5\n(+ x 3))"
        tokens = SchemeTokenizer.tokenize(code_scheme)
        ast = SchemeParser.parse(tokens)
        try:
            scheme_interpreter = SchemeInterpreter(ast)
            scheme_interpreter.execute()
            self.fail("Pas d'erreur levée")
        except SchemeError as e:
            self.assertEqual(str(e), "SyntaxError: Erreur de syntaxe à la ligne 2")

    def test_execute_scheme_lambda(self):
        """Test l'exécution d'un programme Scheme avec une fonction lambda"""
        code_scheme = "(define add (lambda (x y) (+ x y)))\n(display (add 5 3))"
        tokens = SchemeTokenizer.tokenize(code_scheme)
        ast = SchemeParser.parse(tokens)
        try:
            scheme_interpreter = SchemeInterpreter(ast)
            result = scheme_interpreter.execute()
            self.assertEqual(result, "8")
        except SchemeError as e:
            self.fail(f"Erreur lors de l'exécution du code Scheme : {e}")

class TestTokenizer(unittest.TestCase):
    """Classe de tests pour le tokenizer"""

    def test_tokenize(self):
        """Test la tokenization d'un code Scheme"""
        code_scheme = "(define x 5)\n(define y (+ x 3))"
        tokens = SchemeTokenizer.tokenize(code_scheme)
        self.assertEqual(tokens, [("(",), ("define",), ("x",), ("5",), (")",), ("define",), ("y",), ("(",), ("+",), ("x",), ("3",), (")",), ("display",), ("y")])

class TestParser(unittest.TestCase):
    """Classe de tests pour le parser"""

    def test_parse(self):
        """Test la compilation des jetons en ast"""
        tokens = [("(",), ("define",), ("x",), ("5",), (")",), ("define",), ("y",), ("(",), ("+",), ("x",), ("3",), (")",)]
        ast = SchemeParser.parse(tokens)
        self.assertEqual(ast, {
            "type": "program",
            "body": [
                {
                    "type": "define",
                    "name": "x",
                    "value": "5"
                },
                {
                    "type": "define",
                    "name": "y",
                    "value": {
                        "type": "lambda",
                        "args": ["x", "y"],
                        "body": {
                            "type": "plus",
                            "args": ["x", "3"]
                        }
                    }
                }
            ]
        })

if __name__ == "__main__":
    unittest.main()