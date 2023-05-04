import sys
from importlib import import_module
from time import perf_counter


VALID_FILE = 'py_example.py'
TIMES = 100000


def benchmark(package_name):
    def decorator(func):
        def inner():
            try:
                package = import_module(package_name)
            except ImportError:
                return 'not available.'

            start = perf_counter()
            for i in range(TIMES):
                func(package)
            end = perf_counter()

            return end - start
        return inner
    return decorator


@benchmark('yaml')
def run_yaml(package):
    with open(VALID_FILE, 'r') as fin:
        rendered = package.load(fin, Loader=package.SafeLoader)
        return rendered


def run(package_name):
    print(package_name, end=': ')
    print(globals()['run_{}'.format(package_name.lower())]())


def run_all(package_names):
    prompt = 'Running tests with {}...'.format(', '.join(package_names))
    print(prompt)
    print('='*len(prompt))
    for package_name in package_names:
        run(package_name)


def main(*args):
    print('Test document: {}'.format(VALID_FILE))
    print('Test iterations: {}'.format(TIMES))
    if args[1:]:
        run_all(args[1:])
    else:
        run_all(
            [
                # 'yaml'
            ]
        )


if __name__ == '__main__':
    main(*sys.argv)
