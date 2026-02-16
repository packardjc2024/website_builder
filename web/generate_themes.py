import os
from pathlib import Path
from dotenv import load_dotenv
import subprocess


# Deal with filepaths.
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(Path.joinpath(BASE_DIR, '.env'))
themes_prod_filepath = Path.joinpath(BASE_DIR, 'staticfiles', 'themes.css')
themes_dev_filepath = Path.joinpath(BASE_DIR, 'static', 'themes.css')

# Dictionary for settings
settings = {}

# Check if a avbar will be used:
if os.getenv('USE_NAVBAR', 'False').strip().lower() == 'true':
    settings['--navbar-background-color'] = os.getenv('NAVBAR_BACKGROUND_COLOR', 'black')
    settings['--navbar-text-color'] = os.getenv('NAVBAR_TEXT_COLOR', 'white')
    settings['--navbar-border-size'] = os.getenv('NAVBAR_BORDER_SIZE', 'none')
    settings['--navbar-border-style'] = os.getenv('NAVBAR_BORDER_STYLE', 'none')
    settings['--navbar-border-color'] = os.getenv('NAVBAR_BORDER_COLOR', 'none')
    settings['--navbar-height'] = os.getenv('NAVBAR_HEIGHT', '100px')
    settings['--navbar-position'] = 'fixed' if os.getenv('FIXED_NAVBAR', False) else 'relative'
    settings['--navbar-width'] = '100%'
    settings['--navbar-margin-top'] = os.getenv('NAVBAR_MARGIN_TOP', '0px') # Must be px value for calc()
    if os.getenv('ROUNDED_NAVBAR', False).strip().lower() == 'true':
        settings['--navbar-border-radius'] = os.getenv('NAVBAR_BORDER_RADIUS', '20px')
        settings['--navbar-width'] = '95%'

# Check if a footer will be used:
if os.getenv('USE_FOOTER', 'False').strip().lower() == 'true':
    settings['--footer-background-color'] = os.getenv('FOOTER_BACKGROUND_COLOR', 'black')
    settings['--footer-text-color'] = os.getenv('FOOTER_TEXT_COLOR', 'white')
    settings['--footer-border-size'] = os.getenv('FOOTER_BORDER_SIZE', 'none')
    settings['--footer-border-style'] = os.getenv('FOOTER_BORDER_STYLE', 'none')
    settings['--footer-border-color'] = os.getenv('FOOTER_BORDER_COLOR', 'none')
    settings['--footer-height'] = os.getenv('FOOTER_HEIGHT', '50px')

# Create the file content
settings_string = ''
for key, value in settings.items():
    settings_string += f'\t{key}: {value} !important;\n'
css_content = f':root {{\n{settings_string}\n}}'

print(css_content)

# Write the file. 
with open(themes_prod_filepath, 'w') as file:
    file.write(css_content.strip())

with open(themes_dev_filepath, 'w') as file:
    file.write(css_content.strip())
