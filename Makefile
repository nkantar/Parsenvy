.DEFAULT_GOAL := help
.PHONY: help test typecheck formatcheck validate


help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


test: ## run tests and code coverage via pytest and coverage.py
	pipenv run pytest --cov=parsenvy/ --cov-fail-under=100


typecheck: ## run type check via mypy
	pipenv run mypy parsenvy/ --strict


formatcheck: ## run format check via black
	pipenv run black parsenvy/ tests/ --check


validate: ## run tests, code coverage, type check, and format check
	make test
	make typecheck
	make formatcheck
