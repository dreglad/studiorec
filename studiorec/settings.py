# -*- coding: utf-8 -*-
"""
Django settings for studiorec project.

"""

import os
from django.utils.translation import ugettext_lazy as _

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'studiorec36@amdw4$q%jd-$)t4v2ze3#gdu5k3=&_@^82o@xms2&-ra&8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    # 'djangocms_column',
    #'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'cmsplugin_plain_text',

    'analytical',
    'compressor',
    'paintstore',

    'studiorec',
)


ROOT_URLCONF = 'studiorec.urls'
WSGI_APPLICATION = 'studiorec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR,  'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'studiorec', 'static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.datauri.CssDataUriFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]

SITE_ID = 1

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'studiorec', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]



MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'studiorec.ForceDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale', 'cmsplugin_plain_text'),
)

CMS_PLACEHOLDER_CONF = {
#     None: {
#         "plugins": ['TextPlugin'],
#         'excluded_plugins': ['InheritPlugin'],
#     }
    'header-text-large': {
        'name': _("Header text"),
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': ('<h1>Lorem <span class="text-red">ipsum dolor</span> sit amet, consectetur</h1>'
                             '<h2>t vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.<span>&nbsp;</span></h2>'),
                },
            },
        ],
        #'plugins': ['BootstrapContainerPlugin'],
    },
    'header-text-short': {
        'name': _("Header text"),
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': '<h2>Lorem ipsum<span>&nbsp;</span></h2><h1>Dolor sit amet, consectetur</h1>',
                },
            },
        ],
        #'plugins': ['BootstrapContainerPlugin'],
    },
    'footer-col1-title': {
        'name': _("Footer: first column title"),
        'plugins': ['PlaintextPlugin'],
        'limits': {
            'global': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'PlaintextPlugin',
                'values': {
                    'body': _("Footer: first column title"),
                },
            },
        ],
    },
    'footer-col2-title': {
        'name': _("Footer: second column title"),
        'plugins': ['PlaintextPlugin'],
        'limits': {
            'global': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'PlaintextPlugin',
                'values': {
                    'body': _("Footer: second column title"),
                },
            },
        ],
    },
    'footer-col1-content': {
        'name': _("Footer: first column content"),
        # 'plugins': ['TextPlugin', 'PlaintextPlugin'],
    },
    'footer-col2-content': {
        'name': _("Footer: second column content"),
        # 'plugins': ['TextPlugin', 'PlaintextPlugin'],
    },
}

# EXAMPLE
# CMS_PLACEHOLDER_CONF = {
#     None: {
#         "plugins": ['TextPlugin'],
#         'excluded_plugins': ['InheritPlugin'],
#     }
#     'content': {
#         'plugins': ['TextPlugin', 'PicturePlugin'],
#         'text_only_plugins': ['LinkPlugin'],
#         'extra_context': {"width":640},
#         'name': _("Content"),
#         'language_fallback': True,
#         'default_plugins': [
#             {
#                 'plugin_type': 'TextPlugin',
#                 'values': {
#                     'body':'<p>Lorem ipsum dolor sit amet...</p>',
#                 },
#             },
#         ],
#         'child_classes': {
#             'TextPlugin': ['PicturePlugin', 'LinkPlugin'],
#         },
#         'parent_classes': {
#             'LinkPlugin': ['TextPlugin'],
#         },
#     },
#     'right-column': {
#         "plugins": ['TeaserPlugin', 'LinkPlugin'],
#         "extra_context": {"width": 280},
#         'name': _("Right Column"),
#         'limits': {
#             'global': 2,
#             'TeaserPlugin': 1,
#             'LinkPlugin': 1,
#         },
#         'plugin_modules': {
#             'LinkPlugin': 'Extra',
#         },
#         'plugin_labels': {
#             'LinkPlugin': 'Add a link',
#         },
#     },
#     'base.html content': {
#         "plugins": ['TextPlugin', 'PicturePlugin', 'TeaserPlugin'],
#         'inherit': 'content',
#     },
# }


LANGUAGES = (
    ('es', _('es')),
    ('en', _('en')),
)


CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': True,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'es',
            'hide_untranslated': False,
            'name': 'Español',
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': True,
            'name': 'English',
            'redirect_on_fallback': True,
        },
    ]
}

CMS_TEMPLATES = (
    ('home.html', _('Home')),
    ('simple.html', _('Simple page')),
)

CMS_PERMISSION = True

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'data.db'),
    }
}

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {  
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        }
    },
    'root': {
        'handlers': ['console', ],
        'level': 'INFO'
    },
}

try:
    from .local_settings import *
except ImportError:
    pass
