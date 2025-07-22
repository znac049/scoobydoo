import json
from pathlib import Path

from django.forms.widgets import SelectMultiple
from django.template import loader
from django.utils.safestring import mark_safe

from django.conf import settings
from django.utils.module_loading import import_string

class CustomSelectMultiple(SelectMultiple):
    template_name = 'customselect.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)

        return self._render(self.template_name, context, renderer)

