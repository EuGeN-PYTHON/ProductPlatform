# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1861019/data/www/storefoods.ru/ProductPlatform')
sys.path.insert(1, '/var/www/u1861019/data/www/storefoods.ru/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ProductPlatform.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()