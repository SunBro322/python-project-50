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
coverage:
	poetry run pytest --cov=your_package --cov-report=xml:coverage.xml tests/
