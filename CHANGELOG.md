# Parsenvy Changelog


<!--
headers:
Added      - new features
Changed    - changes in existing functionality
Deprecated - soon-to-be removed features
Removed    - now removed features
Fixed      - any bug fixes
Security   - in case of vulnerabilities
-->


## [Unreleased]


## [3.0.0] - 2021-02-21

### Added
- CI with code quality checks
- CD with automatic publishing to PyPI
- Contributing guidelines
- Sphinx generated docs, both locally and on Read the Docs
- Docs for _all_ the things!
- Tests for _all_ the things!
- _**SOME CONTRIBUTORS!!! :D**_

## Changed
- Refactored everything to v3
- Dev env management from Pipenv to Poetry
- Some docs from MD to rST

### Removed
- `dict()`


## [2.1.0] - 2019-05-03

### Deprecated
- `dict()`


## [2.0.10] - 2019-02-15

### Added
- Windows testing via AppVeyor. :)


## [2.0.9] - 2019-02-15

### Fixed
- Package name typo in setup.py.


## [2.0.8] - 2019-02-15

### Changed
- Fixed bad URL in setup.py.


## [2.0.7] - 2019-02-15

### Changed
- Fixed bad version in setup.py.


## [2.0.6] - 2019-02-15

### Changed
- Fixed README type in setup.py.


## [2.0.5] - 2019-02-15

### Changed
- Updated setup.py per most recent docs


## [2.0.4] - 2019-02-15

### Changed
- Moved mypy and Black to dev dependencies.

### Removed
- GitHub templates


## [2.0.3] - 2019-02-15

### Added
- Black code formatter.

### Changed
- Formatted all Python files with Black.


## [2.0.2] - 2019-02-15

### Fixed
- Typing issues were causing Travis CI to fail.

### Changed
- Dev environment is now managed by Pipenv.


## [2.0.1] - 2018-02-11

### Added
- MyPy to Travis CI


## [2.0.0] - 2018-02-11

### Added
- Type hints!

### Removed
- Python 2 support!
- Also support for Python 3.2, 3.3, 3.4, 3.5 and PyPy2.7


## [1.0.2] - 2018-02-11

### Changed
- Fixed bad version linking in the changelog.
- Added release dates to the changelog.
- Added Code of Conduct reference to the README.
- Updated Code of Conduct email.
- Updated first release link from the commit to the release tag.

### Fixed
- Two of the functions returned the wrong thing instead of the default.


## [1.0.1] - 2017-07-31

### Added
- Travis CI
- SayThanks.io badge to README
- Code of Conduct
- Contributing Guidelines
- GitHub issue/PR templates


## [1.0.0] - 2017-04-28

### Changed
- Neater import: `from parsenvy import parsenvy` is now `import parsenvy`.


## [0.1.2] - 2017-04-28

### Added
- Support for Python 3

### Changed
- updated `README.rst`


## [0.1.1] - 2017-03-31

### Changed
- Updated `README.rst`


## [0.1.0] - 2017-03-31

### Added
- Basic functionality


[Unreleased]: https://github.com/nkantar/Parsenvy/compare/3.3.0...HEAD
[3.0.0]: https://github.com/nkantar/Parsenvy/compare/2.1.0...3.0.0
[2.1.0]: https://github.com/nkantar/Parsenvy/compare/2.0.10...2.1.0
[2.0.10]: https://github.com/nkantar/Parsenvy/compare/2.0.9...2.0.10
[2.0.9]: https://github.com/nkantar/Parsenvy/compare/2.0.8...2.0.9
[2.0.8]: https://github.com/nkantar/Parsenvy/compare/2.0.7...2.0.8
[2.0.7]: https://github.com/nkantar/Parsenvy/compare/2.0.6...2.0.7
[2.0.6]: https://github.com/nkantar/Parsenvy/compare/2.0.5...2.0.6
[2.0.5]: https://github.com/nkantar/Parsenvy/compare/2.0.4...2.0.5
[2.0.4]: https://github.com/nkantar/Parsenvy/compare/2.0.3...2.0.4
[2.0.3]: https://github.com/nkantar/Parsenvy/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/nkantar/Parsenvy/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/nkantar/Parsenvy/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/nkantar/Parsenvy/compare/1.0.2...2.0.0
[1.0.2]: https://github.com/nkantar/Parsenvy/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/nkantar/Parsenvy/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/nkantar/Parsenvy/compare/0.1.2...1.0.0
[0.1.2]: https://github.com/nkantar/Parsenvy/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/nkantar/Parsenvy/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/nkantar/Parsenvy/releases/tag/0.1.0
