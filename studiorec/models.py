# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from paintstore.fields import ColorPickerField




class TopImageExtension(PageExtension):
    SIZES_CHOICES = (
        ('short', _('Short')),
        ('large', _('Large'))
    )
    DEFAULT_IMAGE = '..{}images/camera-bg.jpg'.format(settings.STATIC_URL)
    image = models.ImageField(upload_to="headers/", default=DEFAULT_IMAGE,
                            verbose_name=_(u'image'), null=True, blank=True)
    size = models.CharField(_('size'), max_length=16, choices=SIZES_CHOICES, default=SIZES_CHOICES[0])
    color = ColorPickerField(default="#1f3549")



extension_pool.register(TopImageExtension)
