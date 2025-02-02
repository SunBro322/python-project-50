install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
package-reinstall:
	python3 -m pip install  --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
gendiff:
	poetry run gendiff
