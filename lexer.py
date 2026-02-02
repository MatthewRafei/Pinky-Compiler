from tokens import *

class Lexer:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 0
        self.column = 0
        self.tokens = []
        pass

    def advance(self):
        character = self.source[self.current]
        self.current = self.current + 1
        return character
    
    def add_token(self, token_type):
        self.tokens.append(Token(token_type, self.source[self.start:self.current]))

    def tokenize(self):
        while self.current < len(self.source):
            self.start = self.current
            character = self.advance()
            
            if character == "+":
                self.add_token(TOK_PLUS)
            elif character == "-":
                self.add_token(TOK_MINUS)
            elif isinstance(character, int):
                self.add_token(TOK_INTEGER)
            
        return self.tokens
