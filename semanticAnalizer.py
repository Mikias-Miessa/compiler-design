from parser_1 import BinOp, Num
from lexer import INTEGER, FLOAT, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN

class SemanticAnalyzer:
    def __init__(self):
        self.variables = {}  # Dictionary to store variable values

    def analyze(self, node):
        if isinstance(node, BinOp):
            self.analyze(node.left)
            self.analyze(node.right)
        elif isinstance(node, Num):
            # Perform semantic actions for number nodes if needed
            pass
        else:
            raise Exception(f"Invalid node type: {type(node)}")

    def evaluate(self, node):
        if isinstance(node, BinOp):
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)
            if node.op.type == PLUS:
                return left_value + right_value
            elif node.op.type == MINUS:
                return left_value - right_value
            elif node.op.type == MULTIPLY:
                return left_value * right_value
            elif node.op.type == DIVIDE:
                return left_value / right_value
        elif isinstance(node, Num):
            if node.token.type == INTEGER:
                return int(node.value)
            elif node.token.type == FLOAT:
                return float(node.value)
        else:
            raise Exception(f"Invalid node type: {type(node)}")

    def run(self, parsed_line):
        self.analyze(parsed_line)
        result = self.evaluate(parsed_line)
        return result
