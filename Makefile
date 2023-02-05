.PHONY: all, open, options, help, clean

all:
	python3 main.py

open:
	vim -p *.py

options:
	python3 gui_options.py

help:
	python3 gui_help.py

clean:
	@rm -rf __pycache__/
