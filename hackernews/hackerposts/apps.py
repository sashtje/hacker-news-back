from django.apps import AppConfig


class HackerpostsConfig(AppConfig):
    verbose_name = 'Hacker news data'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hackerposts'
