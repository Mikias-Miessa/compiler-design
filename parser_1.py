from lexer import Lexer, Token, INTEGER, FLOAT, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def parse(self):
        return self.expression()

    def expression(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        token = self.current_token

        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == FLOAT:
            self.eat(FLOAT)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expression()
            self.eat(RPAREN)
            return node

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Invalid syntax. Expected {token_type}, found {self.current_token.type}")

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'({self.left}, {self.op}, {self.right})'


class Num:
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f'Num({self.value})'
