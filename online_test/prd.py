from online_test.settings import *


MIGRATION_MODULES = {'yaksh': None}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='asdfkdUmMy_s3cR3t_k3y')
ALLOWED_HOSTS = ['*']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
