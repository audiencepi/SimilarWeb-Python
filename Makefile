deps:
	pip install -r requirements.txt

deps-dev:
	pip install -r requirements_dev.txt

test: clean unit

clean:
	find . -name "*.py[co]" -delete

unit:
	nosetests --with-coverage --cover-package=bigquery_gcs

publish:
	python setup.py sdist upload
