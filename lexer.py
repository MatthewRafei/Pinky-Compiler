from tokens import *

class Lexer:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 0
        self.column = 0
        self.tokens = []
        
    def advance(self):
        character = self.source[self.current]
        self.current = self.current + 1
        return character

    def peek(self):
        return self.source[self.current]

    def lookahead(self, n=1):
        if self.current >= len(self.source):
            return "\0"
        return self.source[self.current + n]

    def match(self, expected):
        if self.current >= len(self.source):
            return False
        if self.source[self.current] != expected:
            return False
        self.current = self.current + 1
        return True
    
    def add_token(self, token_type):
        self.tokens.append(Token(token_type,
                                 self.source[self.start:self.current],
                                 self.line,
                                 self.column))
    
    def tokenize(self):
        while self.current < len(self.source):
            self.start = self.current
            character = self.advance()
            
            match character:
                # New-line, whitespace, tabs, comments, etc.
                case "\n":
                    self.line += 1
                    self.column = 0
                case "\r": self.column = 0
                case "\t": pass
                case " ": pass
                case "#":
                    while (self.peek() != "\n" and
                           not(self.current) >= len(self.source)):
                        self.advance()
                    self.line += 1
                    self.column = 0
                # Single character Symols
                case "(": self.add_token(TOK_LPAREN)
                case ")": self.add_token(TOK_RPAREN)
                case "{": self.add_token(TOK_LCURLY)
                case "}": self.add_token(TOK_RCURLY)
                case "[": self.add_token(TOK_LBRACE)
                case "]": self.add_token(TOK_RBRACE)
                case "+": self.add_token(TOK_PLUS)
                case "-": self.add_token(TOK_MINUS)
                case "*": self.add_token(TOK_STAR)
                case "/": self.add_token(TOK_SLASH)
                case "^": self.add_token(TOK_CARET)
                case "%": self.add_token(TOK_MOD)
                case ";": self.add_token(TOK_SEMICOLON)
                case "?": self.add_token(TOK_QUESTION)
                # Double Character Symbols
                case "=":
                    if self.match("="): self.add_token(TOK_EQ)
                case "~":
                    if self.match("="):
                        self.add_token(TOK_NE)
                        self.column += 1
                    else: self.add_token(TOK_NOT)
                case ">":
                    if self.match("="):
                        self.add_token(TOK_GE)
                        self.column += 1
                    else: self.add_token(TOK_GT)
                case "<":
                    if self.match("="):
                        self.add_token(TOK_LE)
                        self.column += 1
                    else: self.add_token(TOK_LT)
                case ":":
                    if self.match("="):
                        self.add_token(TOK_ASSIGN)
                        self.column += 1
                    else: self.add_token(TOK_COLON)
                # Digits
                case isdigit:
                    while self.peek().isdigit():
                        self.advance()
                    if self.peek() == "." and self.lookahead().isdigit():
                        self.advance()
                        while self.peek().isdigit():
                            self.advance()
                        self.add_token(TOK_FLOAT)
                    else:
                        self.add_token(TOK_INTEGER)
                
            self.column += 1
            
        return self.tokens
