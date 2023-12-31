# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import sys
from pathlib import Path

DOCS = Path(__file__).parent
sys.path.insert(0, str((DOCS / "_extensions").resolve()))


# -- Project information -----------------------------------------------------

project = 'test-sphinx-to-documenter-links'
copyright = '2023, Michael Goerz'
author = 'Michael Goerz'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "fortran_domain",
    "julia_domain",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    # Note: the inventory "python37.inv" was patched to include a reference
    # for :class:`multiprocessing.context.Process`. The patched files was
    # created with the help of https://sphobjinv.readthedocs.io/
    "sympy": ("https://docs.sympy.org/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "qdyn": ("https://ag-koch.gitpages.physik.fu-berlin.de/qdyn/v23.04/", None),
    "QuantumPropagators": ("https://juliaquantumcontrol.github.io/QuantumPropagators.jl/previews/PR66/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
