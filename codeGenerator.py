from lexer import Lexer, Token, INTEGER, FLOAT, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN
from parser_1 import Parser, BinOp, Num

class CodeGenerator:
    def __init__(self):
        self.variable_count = 0
        self.assembly_code = []

    def generate_code(self, node):
        if isinstance(node, BinOp):
            self.generate_code(node.left)
            self.generate_code(node.right)
            self.generate_operation(node.op.type)
        elif isinstance(node, Num):
            self.load_constant(node.value)
        else:
            raise Exception(f"Invalid node type: {type(node)}")

    def generate_operation(self, op_type):
        if op_type == PLUS:
            self.assembly_code.append("ADD")
        elif op_type == MINUS:
            self.assembly_code.append("SUB")
        elif op_type == MULTIPLY:
            self.assembly_code.append("MUL")
        elif op_type == DIVIDE:
            self.assembly_code.append("DIV")

    def load_constant(self, value):
        variable_name = f"var{self.variable_count}"
        self.assembly_code.append(f"LOAD {variable_name}, {value}")
        self.variable_count += 1

    def generate_assembly_code(self, parser):
        tree = parser.parse()
        self.generate_code(tree)

        assembly_code = "\n".join(self.assembly_code)
        return assembly_code
