from pykwalify.cli import run
import json

valid_file = 'json_example.json'
invalid_file = 'json_example_wrong.json'
schema_file = 'json_schema_example.json'

# pykwalify
# rendered = run(
#     {
#         "--data-file": invalid_file,
#         "--schema-file": [schema_file],
#         '--extension': None,
#         '--strict-rule-validation': None,
#         '--fix-ruby-style-regex': None,
#         '--allow-assertions': None,
#         '--encoding': None
#     }
# )

with open(invalid_file, 'r') as fin:
    try:
        rendered = json.loads(fin.read())
        print(rendered)
    except ValueError as e:
        print('invalid json: %s' % e)
