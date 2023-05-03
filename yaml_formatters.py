import pykwalify
import pyyaml

# with open('markdown_example.md', 'r') as fin:
#     rendered = mdformat_black.text(fin.read())
#     rendered = pykwalify.
# print(rendered)

def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None # or: raise