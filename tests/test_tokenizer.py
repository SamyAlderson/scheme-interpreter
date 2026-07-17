import unittest
from src.tokenizer import Tokenizer, TokenException

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize_empty_string(self):
        tokens = self.tokenizer.tokenize("")
        self.assertEqual(tokens, [])

    def test_tokenize_single_char(self):
        tokens = self.tokenizer.tokenize("a")
        self.assertEqual(tokens, ["a"])

    def test_tokenize_multiple_chars(self):
        tokens = self.tokenizer.tokenize("abc")
        self.assertEqual(tokens, ["a", "b", "c"])

    def test_tokenize_whitespace(self):
        tokens = self.tokenizer.tokenize("   a   b   c   ")
        self.assertEqual(tokens, ["a", "b", "c"])

    def test_tokenize_newlines(self):
        tokens = self.tokenizer.tokenize("\na\nb\nc\n")
        self.assertEqual(tokens, ["a", "b", "c"])

    def test_tokenize_parentheses(self):
        tokens = self.tokenizer.tokenize("( a b )")
        self.assertEqual(tokens, ["(", "a", "b", ")"])

    def test_tokenize_brackets(self):
        tokens = self.tokenizer.tokenize("[ a b ]")
        self.assertEqual(tokens, ["[", "a", "b", "]"])

    def test_tokenize_braces(self):
        tokens = self.tokenizer.tokenize("{ a b }")
        self.assertEqual(tokens, ["{", "a", "b", "}"])

    def test_tokenize_invalid_token(self):
        with self.assertRaises(TokenException):
            self.tokenizer.tokenize("abc")

    def test_tokenize_invalid_token_whitespace(self):
        with self.assertRaises(TokenException):
            self.tokenizer.tokenize("a b c")

    def test_tokenize_invalid_token_parentheses(self):
        with self.assertRaises(TokenException):
            self.tokenizer.tokenize("( a b ")

    def test_tokenize_invalid_token_brackets(self):
        with self.assertRaises(TokenException):
            self.tokenizer.tokenize("[ a b ")

    def test_tokenize_invalid_token_braces(self):
        with self.assertRaises(TokenException):
            self.tokenizer.tokenize("{ a b ")

if __name__ == "__main__":
    unittest.main()