from django.contrib import admin
from cityview.models import *

admin.site.register([City, County, State])