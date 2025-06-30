# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'Target Gift Card Balance Guide'
copyright = '2025, Target Gift Card Help'
author = 'Target Gift Card Help Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Easily Check Your Target Gift Card Balance and Use It"

# Optional short title (e.g., for nav bar)
html_short_title = "Target Gift Card Balance Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Uncomment and set your preferred theme if you want to use one
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link in HTML docs
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Enable raw directive globally
raw_enabled = True

# Paths to templates and static files (uncomment if you add your own assets)
# templates_path = ['_templates']
# html_static_path = ['_static']

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
