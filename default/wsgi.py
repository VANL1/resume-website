"""WSGI config for the default project.

The file is also used from ``public_html/cgi-bin/wsgi.py`` via a symlink on
shared hosting. ``realpath`` resolves that symlink, so the project root is
added to ``sys.path`` correctly in both cases.

If the hosting WSGI process does not use the project virtualenv, its
site-packages directory is added explicitly. This keeps the entry point
portable while still working on shared hosting.
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

for site_packages in sorted((BASE_DIR / 'venv' / 'lib').glob('python*/site-packages')):
    if str(site_packages) not in sys.path:
        sys.path.insert(0, str(site_packages))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'default.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
