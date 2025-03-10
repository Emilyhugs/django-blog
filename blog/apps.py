from django.apps import AppConfig


class BlogConfig(AppConfig):
    '''
    This class is used to configure the blog app.

    The BlogConfig class inherits from AppConfig class.

    The BlogConfig class has the following attributes:
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
