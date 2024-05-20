

doctest:  		##@Test perform doctests, add ./docrender after big refactor
	python -m pytest --doctest-modules dashtable


pytest:
	python -m pytest \
		./tests/test.py


test: doctest pytest
