# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin


def page_extra(request):
    page = request.current_page
    if page:
        header_background_image = CMSPlugin.objects.filter(
            placeholder__page=page,
            placeholder__slot='header_background_image',
            plugin_type='FilerImagePlugin',
        ).first()
        if cover_image_plugin:
            return {'header_background_image': cover_image_plugin.filerimage.image}
    return {}
