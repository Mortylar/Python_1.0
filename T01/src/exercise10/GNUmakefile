
INTERPRETER=python3
TARGET=Aparats.py

run:
	$(INTERPRETER) $(TARGET)

run_with_file:
	$(INTERPRETER) $(TARGET) < input

open_all_sources:
	vim $(shell find . -name "*.py")

add:
	git add $(shell find . -name GNUmakefile)
	git add $(shell find . -name "*.py")

clean:
	-rm -rf $(shell find . -name "__pycache__")
