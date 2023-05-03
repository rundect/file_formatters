import mistletoe
import marko
import markdown
import mistune
from mdformat._cli import run as mdformat_run
import commonmark
from pymarkdown import PyMarkdownLint


valid_file = 'md_example.md'
invalid_file = 'md_example_wrong.md'


with open(invalid_file, 'r') as fin:
    rendered_mistletoe = mistletoe.markdown(fin)
print(f"mistletoe: {rendered_mistletoe}")


with open(invalid_file, 'r') as fin:
    reading_file = fin.read()
    rendered_marko = marko.convert(reading_file)
    rendered_markdown = markdown.markdown(reading_file)
    rendered_mistune = mistune.markdown(reading_file)
    rendered_commonmark = commonmark.commonmark(reading_file)
print(f"marko: {rendered_marko}")
print(f"markdown: {rendered_markdown}")
print(f"mistune: {rendered_mistune}")
print(f"commonmark: {rendered_commonmark}")


# mdformat
rendered = mdformat_run(['--check', invalid_file])
print(rendered)

# pymarkdown(pymarkdownlnt)
rendered = PyMarkdownLint().main(['scan', invalid_file])
print(rendered)
