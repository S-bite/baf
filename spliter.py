from parameters import *


def consume_space(tokens, pos):
    npos = pos
    if (npos >= len(tokens)):
        return npos
    while (tokens[npos] == " "):
        npos += 1
        if npos == len(tokens):
            break
    return npos


def get_next_nonspace_token(tokens, pos):
    npos = consume_space(tokens, pos)
    if npos >= len(tokens):
        return (None, npos)
    return tokens[npos], npos


def next_tokens_are_annotation(tokens, pos):
    npos = pos+1
    token, npos = get_next_nonspace_token(tokens, npos)
    print("!", token)
    if token != comemnt_token_begin:
        return False
    token, npos = get_next_nonspace_token(token, npos)
    return token == annotation_prefix


# choosable_tokens:like [a,=,[1,2,3]], a token list with multiple possibilities to be taken
def make_choosable_tokens(tokens):
    choosable_tokens = []
    pos = 0
    while(pos < len(tokens)):
        if next_tokens_are_annotation(tokens, pos):
            # consume comemnt_token_begin
            pos = consume_space(tokens, pos)
            assert(tokens[pos] == comemnt_token_begin)
            pos += 1

            # consume annotation_prefix
            pos = consume_space(tokens, pos)
            assert(tokens[pos] == annotation_prefix)
            pos += 1
            possible_tokens = []
            while tokens[pos] != comemnt_token_end:
                if tokens[pos] != " " and tokens[pos] != annotation_separator:
                    possible_tokens.append(tokens[pos])
            assert(tokens[pos] == comemnt_token_end)
            choosable_tokens.append(possible_tokens)
        else:
            choosable_tokens.append(tokens[pos])
            pos += 1
    return choosable_tokens


def generate_every_possible_code(tokens):
    pass
