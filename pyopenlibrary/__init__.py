"""pyopenlibrary — Open Library book catalog bulk harvester, grouped on harvestkit.

Importing this package imports :mod:`pyopenlibrary.harvest`, which in turn
imports the scraper module so it registers itself with
:mod:`harvestkit.engine` (``@register``).
"""
from pyopenlibrary.version import __version__

import pyopenlibrary.harvest  # noqa: F401  (import for @register side effects)

__all__ = ["__version__"]
