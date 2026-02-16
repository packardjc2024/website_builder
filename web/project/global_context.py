"""
This module sets the variables that can be used in any views context dictionary
for rendering templates, including base.html
"""


from datetime import datetime
from django.conf import settings
from dotenv import load_dotenv
import os
from pathlib import Path
from django.templatetags.static import static


def add_global_context(request):
    """
    Adds a global context for use among all templates, especially base.html.
    """
    SECRETS_PATH = Path.joinpath(settings.BASE_DIR, '.env')
    load_dotenv(SECRETS_PATH)
    return {
        'site_title': os.getenv('SITE_NAME'),
        'copyright_name': os.getenv('COPYRIGHT_NAME'),
        'copyright_year': os.getenv('COPYRIGHT_YEAR', datetime.now().year),
        'site_logo_url': static('site_pictures/logo.png'),
        'use_account': settings.USE_ACCOUNT,
        'use_navbar': os.getenv("USE_NAVBAR", "False").strip().lower() == "true",
        'use_footer': os.getenv("USE_FOOTER", "False").strip().lower() == "true",
        'attributions': [
            {
                'name': 'test name',
                'text': 'test text',
                'link': 'test link',
            },
        ],
    }