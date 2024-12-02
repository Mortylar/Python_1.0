
INTERPRETER=python3
TARGET=main.py

run:
	$(INTERPRETER) $(TARGET) < input.txt

open_all_sources:
	vim $(shell find . -name "*.py")

add:
	git add $(shell find . -name GNUmakefile)
	git add $(shell find . -name "*.py")

clean:
	-rm -rf $(shell find . -name "__pycache__")
