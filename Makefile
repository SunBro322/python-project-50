Gendiff-json:
	poetry run gendiff file1.json file2.json

Gendiff-yaml:
	poetry run gendiff file1.yaml file2.yaml

Test:
	poetry run pytest

install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	  poetry run flake8 gendiff
