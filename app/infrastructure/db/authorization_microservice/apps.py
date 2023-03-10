from django.apps import AppConfig

from app.infrastructure.db.settings.settings import BASE_DJANGO_APP_PATH


class AuthorizationMicroserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = BASE_DJANGO_APP_PATH + 'authorization_microservice'
