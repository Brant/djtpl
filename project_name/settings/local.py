from .base import *


if DEBUG:
    MIDDLEWARE_CLASSES = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # 'django.middleware.cache.UpdateCacheMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        # 'django.middleware.cache.FetchFromCacheMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    INSTALLED_APPS += ('debug_toolbar', )
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
