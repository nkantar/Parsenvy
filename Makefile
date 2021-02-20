.DEFAULT_GOAL := help
.PHONY: help formatcheck lint docstringcheck dockbuildcheck typecheck test test-watch covcheck

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

formatcheck: ## check formatting with black
	poetry run black --check .

lint: ## lint with flake8
	poetry run flake8 .

docstringcheck: ## check code docs with pydocstyle
	poetry run pydocstyle .

docbuildcheck: ## check documentation site build
	echo "TODO"  # TODO

typecheck: ## check type hints with mypy
	poetry run mypy --strict .

test: ## run tests with pytest
	poetry run pytest --cov=parsenvy -vv

test-watch: ## watch tests with pytest-watch
	poetry run pytest-watch -- --cov=parsenvy -vv

covcheck: ## check code coverage level
	poetry run coverage report --fail-under=100
