#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin
from apps.tree.models import *

admin.site.register(Tree)
admin.site.register(Question)
admin.site.register(Answer)
