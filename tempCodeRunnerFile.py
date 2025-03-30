    def test_basic_integers(self):
        self.lexer.input('1934')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, 1934)