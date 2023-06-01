import re

# Token types
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
NEWLINE = 'NEWLINE'
EOF = 'EOF'

# Regular expression patterns
patterns = [
    (r'\d+\.\d+', FLOAT),  # Matches floating-point numbers
    (r'\d+', INTEGER),  # Matches integers
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
    (r'\n', NEWLINE),
    (r'\s+', None),  # Ignore whitespace
    (r'#.*?(?=\n|$)', None)  # Ignore comments starting with '#'
]

class Lexer:
    def __init__(self, text):
        self.lines = text.splitlines()
        self.current_line = 0
        self.pos = 0
        self.current_token = None

    def get_next_token(self):
        if self.current_line >= len(self.lines):
            return Token(EOF, None)

        line = self.lines[self.current_line]
        if self.pos >= len(line):
            self.current_line += 1
            self.pos = 0
            return Token(NEWLINE, '\n')

        text = line[self.pos:]
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(text)
            if match:
                value = match.group()
                if token_type is None:
                    self.pos += match.end()
                    return self.get_next_token()  # Skip comments and whitespace
                token = Token(token_type, value)
                self.pos += match.end()
                return token

        char = text[0]
        self.pos += 1
        return Token('INVALID', char)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'{self.type}: {self.value}'