import mistletoe
import marko
from marko import Markdown
import markdown
import mistune
from mdformat._cli import run as mdformat_run
import commonmark
from pymarkdown import PyMarkdownLint

from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from markdown_it import MarkdownIt

valid_file = 'md_example.md'
invalid_file = 'md_example_wrong.md'


# with open(invalid_file, 'r') as fin:
#     rendered_mistletoe = mistletoe.markdown(fin)
#     print(f"mistletoe: {rendered_mistletoe}")

# with open(invalid_file, 'r') as fin:
#     with mistletoe.HTMLRenderer() as renderer:
#         doc = mistletoe.Document(fin)
#         rendered_mistletoe_ast = renderer.render(doc)
#     print(f"mistletoe_ast: {rendered_mistletoe_ast}")


# with open(invalid_file, 'r') as fin:
#     reading_file = fin.read()
#     rendered_marko = marko.convert(reading_file)
#     rendered_markdown = markdown.markdown(reading_file)
#     rendered_mistune = mistune.markdown(reading_file)
#     rendered_commonmark = commonmark.commonmark(reading_file)
# print(f"marko: {rendered_marko}")
# print(f"markdown: {rendered_markdown}")
# print(f"mistune: {rendered_mistune}")
# print(f"commonmark: {rendered_commonmark}")


# mdformat
# rendered_mdformat = mdformat_run(['--check', invalid_file])
# print(f"mdformat: {rendered_mdformat}")


# markdown_it_py
# with open(invalid_file, 'r') as fin:
#     md = (
#         MarkdownIt(
#             'commonmark',
#             {
#                 'breaks': True,
#                 'html': True
#             }
#         )
#         .use(front_matter_plugin)
#         .use(footnote_plugin)
#         .enable('table')
#     )
#     reading_file = fin.read()
#     rendered_markdown_it_py = md.parse(reading_file)
#     html_text = md.render(reading_file)
# print(f"markdown_it_py: {html_text}")


# pymarkdown(pymarkdownlnt)
rendered = PyMarkdownLint().main(['scan', valid_file])
print(f"pymarkdownlnt: {rendered}")
