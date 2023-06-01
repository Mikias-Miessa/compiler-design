from lexer import Lexer
from parser_1 import Parser
from semanticAnalizer import SemanticAnalyzer

# Read code from file
filename = input("Enter the name of the file containing the code: ")
with open(filename, 'r') as file:
    code = file.read()

lexer = Lexer(code)
parser = Parser(lexer)
analyzer = SemanticAnalyzer()

parsed_line = parser.parse()
result = analyzer.run(parsed_line)
print(f"Result: {result}")


