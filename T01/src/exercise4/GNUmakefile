
INTERPRETER=python3
TARGET=Pascal.py

run:
	$(INTERPRETER) $(TARGET)

open_all_sources:
	vim $(shell find . -name "*.py")

add:
	git add $(shell find . -name GNUmakefile)
	git add $(shell find . -name "*.py")

clean:
	-rm -rf $(shell find . -name "__pycache__")
