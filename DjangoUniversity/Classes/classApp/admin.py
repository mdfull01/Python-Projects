from django.contrib import admin
# import djangoClass we created
from .models import djangoClasses

# register djangoClasses model
admin.site.register(djangoClasses)
