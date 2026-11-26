"""Individual contribution; adapted from the FG-TIDA specification template."""

project = 'FP-TIDA-INPUTS'
release = '0.1'
author = 'Zhiyuan Ji (Chi20)'
copyright = '2026, Zhiyuan Ji; template: Debora Comparin'
language = 'en'
source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'
exclude_patterns = ['_*.rst', '*/_*.rst']
extensions = ['sphinx_copybutton']
numfig = True
pygments_style = 'colorful'
templates_path = ['_templates']
html_theme = 'furo'
html_title = 'FP-TIDA-INPUTS: individual contribution v0.1'
html_static_path = ['_static']
html_css_files = ['osia-furo.css']
html_js_files = ['osia-sidebar.js']
html_theme_options = {'sidebar_hide_name': False}
html_show_sourcelink = True
today = '26 November 2026'
latex_documents = [
    (master_doc, 'contribution.tex',
     'Versioned approval and authority provenance: Foundation Protocol reference inputs',
     author, 'manual'),
]
latex_elements = {'papersize': 'a4paper', 'pointsize': '10pt'}
