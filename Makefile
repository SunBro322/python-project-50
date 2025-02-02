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

codeclimate:  ## Отправить отчёт в CodeClimate (локально)
	curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
	chmod +x ./cc-test-reporter
	./cc-test-reporter before-build
	$(MAKE) coverage
	./cc-test-reporter format-coverage -t coverage.py coverage.xml
	CC_TEST_REPORTER_ID=$${CC_TEST_REPORTER_ID} ./cc-test-reporter upload-coverage
