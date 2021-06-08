PYTHON = python3
PYTHON_FILES := $(shell find . -name "*.py")

.PHONY = format check

format:
	isort $(PYTHON_FILES)
	black $(PYTHON_FILES)

check:
	isort -c $(PYTHON_FILES)
	black --check $(PYTHON_FILES)
	mypy $(PYTHON_FILES)
	pylint $(PYTHON_FILES)