from django.contrib import admin
import django.contrib.auth.models as default
from . import models

admin.site.register([models.Test])

admin.site.unregister([default.User, default.Group])
