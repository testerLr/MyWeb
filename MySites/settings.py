"""
Django settings for MySites project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd^cg&zhekma_br$b39#r7b9hwkkn#!g-gwoo6laon21hdghy+v'

# SECURITY WARNING: don't run with debug turned on in production!
# 打开调试模式
DEBUG = True
# DEBUG = False
# 允许其它IP地址访问服务器
ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SitesApp',
# 注册富文本应用
    'tinymce',
#     注册xadmin应用
    'xadmin',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #     注册自定义的中间件
    'middleware.MyMiddleware.SitesAppMiddleware',
]

ROOT_URLCONF = 'MySites.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
		,
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

WSGI_APPLICATION = 'MySites.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 使用MySQL数据库
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名称
        'NAME': 'MySites',
        # 账号和密码
        'USER': 'root',
        'PASSWORD': '123456',
        # IP和端口
        'HOST': 'localhost',
        'PORT': '3306',
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
#全部静态资源存放地址
# STATIC_ROOT = os.path.join(BASE_DIR,'static')
# 添加静态资源路由地址
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),

]
# 配置框架的上传文件保存位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'static','uploads')

# 配置需要登录才能访问的路由
LOGIN_VISIT = [
    '/app/mine/',
    '/app/review/',
]
VISIT_PATH = {}
# 自定义的黑名单
BLACK_LIST = [
    '192.168.116.1',
]

# 自定义的VIP名单
VIP_LIST = [
    '127.0.0.1',
]

# 缓存设置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'sitesappcachetable',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        },

        'TIMEOUT': 60,
    },

    'redis_special': {
        "BACKEND": "django_redis.cache.RedisCache",
        # 123456为redis密码
        "LOCATION": "redis://:123456@127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },

        'TIMEOUT': 60,
    },

}

# 以字典形式配置富文本框架tinymce
# 作用于管理后台中的富文本编辑器
TINYMCE_DEFAULT_CONFIG = {

    # 使用高级主题,备选项还有简单主题
    'theme': 'advanced',
    # 'theme': 'simple',

    # 必须指定富文本编辑器(RTF=rich text format)的宽高
    'width': 800,
    'height': 600,

    # 汉化
    'language': 'zh',

    # 自定义常用的固定样式
    'style_formats': [
        # title=样式名称
        # styles=自定义css样式
        # inline:xxx = 将加样式后的文本放在行内元素中显示
        # block:xxx = 将加样式后的文本放在块级元素中显示
        {'title': 'Bold text', 'inline': 'b'},
        {'title': 'Red text', 'inline': 'span', 'styles': {'color': '#ff0000'}},
        {'title': 'Red header', 'block': 'h1', 'styles': {'color': '#ff0000'}},
        {'title': 'Example 1', 'inline': 'span', 'classes': 'example1'},
        {'title': 'Example 2', 'inline': 'span', 'classes': 'example2'},
        {'title': 'Table styles'},
        {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow1'}
    ],
}

