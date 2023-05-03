import black
import importlib
mdformat_black = importlib.import_module("mdformat-black")
mdformat_config = importlib.import_module("mdformat-config")


with open('markdown_example.md', 'r') as fin:
    rendered = mdformat_black.text(fin.read())
print(rendered)

