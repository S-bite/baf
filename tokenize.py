import sys


def tokenize(src):
    tokens = []
    pos = 0
    while pos < len(src):
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
        tokens.append(token)
    return tokens


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        src = f.read()
        tokens = tokenize(src)
        print("".join(tokens))


main()
