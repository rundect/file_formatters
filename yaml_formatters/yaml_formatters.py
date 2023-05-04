from pykwalify.cli import run
from mdformat._cli import run as mdformat_run
from yamllint.cli import run as yamllint_run
from yaml import load, dump

valid_file = 'yaml_example.yaml'
invalid_file = 'yaml_example_wrong.yaml'
schema_file = 'yaml_example.schema.yaml'

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
# print(f"pykwalify: {rendered}")


# mdformat
# rendered_mdformat = mdformat_run(['--check', invalid_file])
# print(f"mdformat: {rendered_mdformat}")

# yamllint
rendered_yamllint = yamllint_run([valid_file])
print(f"yamllint: {rendered_yamllint}")
