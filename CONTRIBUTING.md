# Contributing to Parsenvy

Hi! First of all, thank you for contributing. :heart:

All of the usual sorts of contributions are welcome: bug reports, patches, and feedback.
Feel free to [browse existing issues](https://github.com/nkantar/Parsenvy/issues) or [create a new one](https://github.com/nkantar/Parsenvy/issues/new).

Participation in this project in any way requires complying with the [Code of Conduct](CODE_OF_CONDUCT.md).


## Got a problem?

You're welcome to [create an issue](https://github.com/nkantar/Parsenvy/issues/new), but please [search existing ones](https://github.com/nkantar/Parsenvy/issues) first to see if it's been discussed before.


## Want to submit some code or docs?

Great! 
If you're intersted in tackling an [existing issue](https://github.com/nkantar/Parsenvy/issues), comment on one to make sure you're on the right track.
If it's an idea you have or a problem not captured in an issue, [create one](https://github.com/nkantar/Parsenvy/issues/new) and let's align.


### Dev setup

Requirements:

- Python 3.6 or higher
- [Poetry](https://python-poetry.org/)

Once you have those two, install project dependencies with:

```
poetry install
```

At this point you should be able to make changes to the codebase and run things.

Speaking of running things, there are a number of code quality checks that get run on every pull request.
You are encouraged to run them locally as you work for a much faster feedback loop.

| Command | What it does |
|:------- |:------------ |
| `make formatcheck` | Run the `black` formatter with the `--check` flag to validate the source is formatted correctly. |
| `make lint` | Run the `flake8` linter to validate there are no linter errors in the source. |
| `make doccheck` | Run the `pydocstyle` docstring format checker to validate the docstrings are complete and standardized. _Currently disabled._ |
| `make docs` | Run the Sphinx documentation site builder to validate the docs build successfully. |
| `make typecheck` | Run the `mypy` type checker to validate the type annotations are valid. _Currently disabled._ |
| `make test` | Run tests to validate they all pass. |
| `make covcheck` | Calculate test coverage to validate all code paths are executed at least once. |
