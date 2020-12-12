from parameters import *


def consume_space(tokens, pos):
    npos = pos
    if (npos >= len(tokens)):
        return npos
    while (tokens[npos] == " "):
        npos += 1
        if npos == len(tokens):
            break
   # assert(npos == len(tokens) or tokens[npos] != " ")
    return npos


def get_next_nonspace_token(tokens, pos):
    npos = consume_space(tokens, pos+1)
    if npos >= len(tokens):
        return (None, npos)
    return tokens[npos], npos


# checks if tokens[next_token_index] is comment_begin and following non-space token is annotation_prefix
def next_tokens_are_annotation(tokens, next_token_index):
    if tokens[next_token_index] != comemnt_token_begin:
        return False
    token, next_token_index = get_next_nonspace_token(tokens, next_token_index)
    return token == annotation_prefix


# choosable_tokens:like [a,=,[1,2,3]], a token list with multiple possibilities to be taken
def make_choosable_tokens(tokens):
    choosable_tokens = []
    next_token_index = 0
    while (next_token_index < len(tokens)):
        if next_tokens_are_annotation(tokens, next_token_index):
            # consume comemnt_token_begin
            assert(tokens[next_token_index] == comemnt_token_begin)
            _, next_token_index = get_next_nonspace_token(
                tokens, next_token_index)

            # consume annotation_prefix
            assert(tokens[next_token_index] == annotation_prefix)
            _, next_token_index = get_next_nonspace_token(
                tokens, next_token_index)

            possible_tokens = []
            while tokens[next_token_index] != comemnt_token_end:
                if tokens[next_token_index] != " " and tokens[next_token_index] != annotation_separator:
                    possible_tokens.append(tokens[next_token_index])
                next_token_index += 1
             # consume comment_end
            assert (tokens[next_token_index] == comemnt_token_end)
            next_token_index += 1
            choosable_tokens.append(possible_tokens)
        else:
            choosable_tokens.append(tokens[next_token_index])
            next_token_index += 1
    return choosable_tokens
