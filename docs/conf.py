"""Sphinx configuration."""
import os
import sys


sys.path.insert(0, os.path.abspath("../.."))


project = "Data Science Portfolio"
author = "Moritz Mistol"
copyright = "2022, Moritz Mistol"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
autosummary_generate = True
