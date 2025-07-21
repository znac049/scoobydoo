import json
from pathlib import Path

from django import forms
from django.template import loader
from django.utils.safestring import mark_safe

class CustomMultiSelect(forms.Widget):
    template_name = 'zob.html'

    def get_context(self, name, value, attrs=None):
        return {
            'widget': {
                'name': name,
                'value': value,
            }
        }

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        context['bob'] = '<b>Bob!</b>'
        context['attrs'] = attrs

        print(f"value={value}, attrs={attrs}")
        print(json.dumps(context, indent=2))
        # print(self.get_form())

        template = loader.get_template(self.template_name).render(context)

        return mark_safe(template)

