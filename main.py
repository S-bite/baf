from tokenizer import tokenize
from spliter import make_choosable_tokens
from generator import generate_every_possible_code
import sys


def main():
    if (len(sys.argv) != 2):
        print(f"Usage {sys.argv[0]} target_file")
        exit(0)
    input_file_name = sys.argv[1]
    with open(input_file_name, "r") as rf:
        src = rf.read()
        possible_codes = generate_every_possible_code(
            make_choosable_tokens(tokenize(src)))
        for i in range(len(possible_codes)):
            code = possible_codes[i]
            output_file_name = f"{input_file_name}_{str(i)}.tmp"
            with open(output_file_name, "w") as wf:
                wf.write(code)


if __name__ == "__main__":
    main()
