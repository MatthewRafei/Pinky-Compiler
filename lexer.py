from tokens import *

class Lexer:
    def __int__(source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 0
        self.column = 0
        self.tokens = []

    def advance(self):
        character = self.source[self.curr]
        self.current = self.current + 1
        return character

    def tokenize(self):
        while self.current < len(self.source):
            self.start = self.current
            character = self.advance()
            
            if character == "+":
                self.tokens.append(Token(TOK_PLUS, self.source[self.start:self.current]))
            
        return self.tokens
