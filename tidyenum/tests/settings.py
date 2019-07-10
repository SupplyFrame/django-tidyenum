SECRET_KEY = "test"
DEBUG = True

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "tidyenum",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    }
}

STATIC_URL = "/static/"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


MIGRATION_MODULES = {
    # This lets us skip creating migrations for the test models as many of
    # them depend on one of the following contrib applications.
    'tidyenum': None
}
