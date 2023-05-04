from mdformat._cli import run as mdformat_run
from black import main
import yapf


valid_file = 'py_example.py'
invalid_file = 'py_example_wrong.py'


# mdformat
# rendered_mdformat = mdformat_run(['--check', valid_file])
# print(f"mdformat: {rendered_mdformat}")


# black
# with open(valid_file, 'r') as fin:
#     code = fin.read()
#     rendered_black = main(valid_file,)
#     print(f"black: {rendered_black}")


