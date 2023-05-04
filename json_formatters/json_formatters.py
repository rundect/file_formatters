import json
from pykwalify.cli import run
from json_checker import Checker
from mdformat._cli import run as mdformat_run

valid_file = 'json_example.json'
invalid_file = 'json_example_wrong.json'
schema_file = 'json_schema_example.json'

# pykwalify
rendered = run(
    {
        "--data-file": invalid_file,
        "--schema-file": [schema_file],
        '--extension': None,
        '--strict-rule-validation': None,
        '--fix-ruby-style-regex': None,
        '--allow-assertions': None,
        '--encoding': None
    }
)
print(f"pykwalify: {rendered}")


# json
with open(valid_file, 'r') as fin:
    try:
        rendered = json.loads(fin.read())
        print(f"json: {json.dumps(rendered, indent=4)}")
    except ValueError as e:
        print('invalid json: %s' % e)


# json_checker
expected_schema = {
    "name": str,
    "email": str,
    "age": int,
    "gender": str,
    "favorite": list
}
with open(valid_file, 'r') as fin:
    current_data = json.load(fin)
    checker = Checker(expected_schema)
    result = checker.validate(current_data)
    print(f"json_checker: {result}")


# mdformat
rendered_mdformat = mdformat_run(['--check', invalid_file])
print(f"mdformat: {rendered_mdformat}")
