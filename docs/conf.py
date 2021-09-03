import os
import sys
sys.path.insert(0, os.path.abspath('../hermione/module_templates/__IMPLEMENTED_BASE__/src/'))

project = "Hermione"

extensions = [
    "myst_parser",
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon'
]
# html_theme = "sphinx_rtd_theme"
source_suffix = [".rst", ".md"]
