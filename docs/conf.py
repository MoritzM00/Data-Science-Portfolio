"""Sphinx configuration."""
project = "Data Science Portfolio"
author = "Moritz Mistol"
copyright = "2022, Moritz Mistol"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

napoleon_google_docstring = False
