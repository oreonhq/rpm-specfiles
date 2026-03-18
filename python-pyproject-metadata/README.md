# python-pyproject-metadata

[This package](https://github.com/FFY00/python-pyproject-metadata) contains a
dataclass for [PEP 621](https://peps.python.org/pep-0621/) metadata with
support for core metadata generation.

This project does not implement the parsing of `pyproject.toml` containing
PEP 621 metadata.  Instead, given a Python data structure representing
PEP 621 metadata (already parsed), it will validate this input and
generate a PEP 643-compliant metadata file (e.g. PKG-INFO).
