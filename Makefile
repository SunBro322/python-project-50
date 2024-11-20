Gendiff-json:
	poetry run gendiff file1.json file2.json

Gendiff-yaml:
	poetry run gendiff file1.yaml file2.yaml

Gendiff-stylish:
	poetry run gendiff -f stylish file1.json file2.json

Gendiff-plain:
	poetry run gendiff -f plain file1.json file2.json

test:
	poetry run pytest

install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	  poetry run flake8 gendiff


test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml


