install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install  --force-reinstall dist/*.whl
lint:
	poetry run flake8 .
pytest:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
gendiff:
	poetry run gendiff --cov-report xml tests