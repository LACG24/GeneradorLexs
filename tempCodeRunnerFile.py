    # def test_wrong_integers(self):
    #     self.lexer.input('1__934')
    #     token = self.lexer.token()
    #     self.assertEqual(token.type, 'INT')
    #     self.assertNotEqual(token.value, 1934)
    #     self.assertRaises(lex.LexError, self.lexer.token)