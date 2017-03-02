from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import TopImageExtension


class TopImageExtensionAdmin(PageExtensionAdmin):
    pass


admin.site.register(TopImageExtension, TopImageExtensionAdmin)