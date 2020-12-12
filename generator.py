from parameters import *


def generate_every_possible_code(choosable_tokens):
    possible_codes = [""]
    for choosable_token in choosable_tokens:
        updated_possible_codes = []
        for possible_code in possible_codes:
            for token in choosable_token:
                updated_possible_codes.append(possible_code + token)
        possible_codes = updated_possible_codes
    return possible_codes
