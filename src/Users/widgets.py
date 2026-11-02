from django.forms import widgets
from django.utils.safestring import mark_safe


class CustomPictureImageFieldWidget(widgets.ClearableFileInput):

    def value_from_datadict(self, data, files, name):
        upload = files.get(name)
        # new file takes priority over clear checkbox
        if upload:
            return upload
        return super().value_from_datadict(data, files, name)

    def render(self, name, value, attrs=None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)
        img_html = ''
        if value and hasattr(value, 'url'):
            img_html = (
                f'<div style="display:flex; justify-content:center; margin-bottom:12px;">'
                f'<img src="{value.url}" '
                f'style="width:120px; height:120px; object-fit:cover; '
                f'border-radius:50%; border:3px solid #dee2e6;" />'
                f'</div>'
            )
        return mark_safe(f'{img_html}{default_html}')