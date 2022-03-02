"""
bag/apps.py: app config file for bag app.
"""

from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    bag app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
