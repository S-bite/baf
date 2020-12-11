import sys
from parameters import *


def get_ident(src, pos):
    ch = src[pos]
    token = ''
    if (ch.isalnum()):
        while (ch.isalnum()):
            token += ch
            pos += 1
            ch = src[pos]
    else:
        token = ch
        pos += 1
    return token, pos


def tokenize(src):
    tokens = []
    pos = 0
    while pos < len(src):
        for token in tokens_for_split:
            if (src[pos:].startswith(token)):
                pos += len(token)
                tokens.append(token)
                break
        else:
            token, pos = get_ident(src, pos)
            tokens.append(token)
    return tokens


def get_block_comment(tokens):
    pass


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        src = f.read()
        tokens = tokenize(src)
        show = False
        for token in tokens:
            if (token == comemnt_token_begin):
                show = True
                continue
            elif (token == comemnt_token_end):
                show = False
                continue
            if (show):
                print(token)


if __name__ == "__main__":
    main()
