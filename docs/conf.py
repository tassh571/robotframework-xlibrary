# conf.py

# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'XpiumLibraryFlutter'
author = 'Tassana Khrueawan'
version = '0.0.5'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Includes documentation from docstrings
    'sphinx.ext.coverage', # Checks documentation coverage
    'sphinx.ext.napoleon', # Supports Google and NumPy style docstrings
    'sphinx.ext.viewcode', # Includes source code links in documentation
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
