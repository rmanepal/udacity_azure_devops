hello:
	echo "this is my first make command"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	python -m pylint --disable=R,C hello.py

test:
	python -m pytest -vv test_hello.py

all: hello install lint test
