migration.remove_files:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

git.init_pre_commit:
	pre-commit install
	pre-commit install --hook-type pre-push

requirements.compile:
	pip-compile requirements/dev.in
	pip-compile requirements/prod.in
