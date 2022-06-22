# flake8-pep518

Flake8 plugin that allows specifying config in pyproject.toml.

There are a lot of projects that do essentially the same thing, but only this one doesn't make you change the command. Also, it's deadly simple:

```bash
pip install flake8-pep518
```

And that's it!

## Usage

Install the plugin with the command above and move your Flake8 config to `pyproject.toml`.

```setup.cfg
[flake8]
ignore = E231, E241
per-file-ignores =
    __init__.py:F401
max-line-length = 88
count = true
```

Rename `[flake8]` section to `[tool.flake8]` and convert everything else to TOML format.

```pyproject.toml
[tool.flake8]
ignore = ['E231', 'E241']
per-file-ignores = [
    '__init__.py:F401',
]
max-line-length = 88
count = true
```

Run Flake8 as usuall.

```bash
flake8
```

## Inspiration

Inspired by [Flake8], [Flake9], [FlakeHeaven] and [Flake8-pyproject].

## License

**flake8-pep518** is licensed under the MIT. Please see [License.md] for more information.

[Flake8]: https://github.com/pycqa/flake8
[Flake9]: https://gitlab.com/retnikt/flake9
[FlakeHeaven]: https://github.com/flakeheaven/flakeheaven
[Flake8-pyproject]: https://github.com/john-hen/Flake8-pyproject
[License.md]: https://github.com/aleksul/flake8-pep518/blob/main/LICENSE
