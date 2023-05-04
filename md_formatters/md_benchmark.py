import sys
from importlib import import_module
from time import perf_counter


TEST_FILE = 'md_example.md'
TIMES = 1000


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


@benchmark('markdown')
def run_markdown(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        return package.markdown(fin.read(), extensions=['fenced_code', 'tables'])


@benchmark('mistune')
def run_mistune(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        return package.markdown(fin.read())


@benchmark('commonmark')
def run_commonmark(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        return package.commonmark(fin.read())


@benchmark('mistletoe')
def run_mistletoe(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        return package.markdown(fin)


@benchmark('mdformat')
def run_mdformat(package):
    from mdformat._cli import run as mdformat_run
    return mdformat_run(['--check', TEST_FILE])


@benchmark('marko')
def run_marko(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        return package.convert(fin.read())


@benchmark('markdown_it')
def run_markdown_it(package):
    with open(TEST_FILE, 'r', encoding='utf-8') as fin:
        from mdit_py_plugins.front_matter import front_matter_plugin
        from mdit_py_plugins.footnote import footnote_plugin
        md = (
            package.MarkdownIt(
                'commonmark',
                {
                    'breaks': True,
                    'html': True
                }
            )
            .use(front_matter_plugin)
            .use(footnote_plugin)
            .enable('table')
        )
        reading_file = fin.read()
        rendered_markdown_it_py = md.parse(reading_file)
        html_text = md.render(reading_file)
        return html_text


@benchmark('pymarkdown')
def run_pymarkdown(package):
    # TODO: закомментировать 488-489 строки (sys.exit(1)) в pymarkdown/main.py
    from pymarkdown import PyMarkdownLint
    rendered = PyMarkdownLint().main(['scan', TEST_FILE])
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
    print('Test document: {}'.format(TEST_FILE))
    print('Test iterations: {}'.format(TIMES))
    if args[1:]:
        run_all(args[1:])
    else:
        run_all(
            [
                # 'markdown',
                # 'mistune',
                # 'commonmark',
                # 'mistletoe',
                'mdformat',
                # 'marko',
                # 'markdown_it',
                # 'pymarkdown'
            ]
        )


if __name__ == '__main__':
    main(*sys.argv)
