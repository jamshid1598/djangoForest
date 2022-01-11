from proroot.settings.base import *



# override everything here


ALLOWED_HOSTS = ['http://127.0.0.1:8000', '*']




# django-forestadmin configuration
FOREST = {
    'FOREST_URL': 'https://api.forestadmin.com',
    'APPLICATION_URL': 'http://127.0.0.1:8000',
    'FOREST_ENV_SECRET': '39a30a2da8558e79d66a54a539d1ddd1d216e38284c0f8dedc70108bc4b7afc6',
    'FOREST_AUTH_SECRET': '9e1ebe9fefe3d5c6a81623d8b2bdb4fc307cdb6c83f367a4'
}
APPEND_SLASH=False