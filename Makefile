.DEFAULT_GOAL := help
.PHONY: help formatcheck lint doccheck docs typecheck test test-watch covcheck

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

formatcheck: ## check formatting with black
	poetry run black --check parsenvy/parsenvy.py

lint: ## lint with flake8
	poetry run flake8 parsenvy/parsenvy.py

doccheck: ## check code docs with pydocstyle
	poetry run pydocstyle parsenvy/parsenvy.py

docs: ## build docs site
	poetry run make -C docs html

typecheck: ## check type hints with mypy
	poetry run mypy --strict parsenvy/parsenvy.py

test: ## run tests with pytest
	poetry run pytest --cov -vv

test-watch: ## watch tests with pytest-watch
	poetry run pytest-watch -- --cov -vv

covcheck: ## check code coverage level
	poetry run coverage report --fail-under=100
