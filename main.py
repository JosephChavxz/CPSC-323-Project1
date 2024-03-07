import re

token_regex = {
    'keyword': r'while',
    'identifier': r'[a-zA-Z_]\w*',
    'operator': r'[=<>]',
    'separator': r'[();]',
    'integer' : r'\d+'
}

def lexer(input_file):
    tokens = []

    with open(input_file, 'r') as file:
        source_code = file.read()

    for token_type, regex in token_regex.items():
        for match in re.finditer(regex, source_code):
            tokens.append((token_type, match.group()))

    return tokens

def print_tokens(tokens):
    print("Token\tLexeme")
    for token, lexeme in tokens:
        print(f"{token}\t{lexeme}")

if __name__ == "__main__":
    input_file = "input_scode.txt"
    tokens = lexer(input_file)
    print_tokens(tokens)
