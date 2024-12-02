
INTERPRETER=python3
INPUT=input

run:
ifeq ("","$(wildcard ./$(stage)/$(INPUT))")
	cd $(stage) && make run
else
	cd $(stage) && make run_with_file
endif

open_all_sources:
	vim $(shell find . -name "*.py")

add:
	git add $(shell find . -name GNUmakefile)
	git add $(shell find . -name "*.py")

clean:
	-rm -rf $(shell find . -name "__pycache__")
