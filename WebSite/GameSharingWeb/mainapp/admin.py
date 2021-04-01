from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# class NotebookAdminForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = mark_safe(
#             """'<span style="color:red; font-size:12px;" >При закгрузке изображения больше чем {}x{}, оно будет обрезано автоматически </span>'""".format(
#                 *Product.MAX_RESOLUTION
#             )
#         )
#
# class NotebookAdmin(admin.ModelAdmin):
#     form = NotebookAdminForm
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'category':
#             return ModelChoiceField(Category.objects.filter(slug='Notebooks'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#
# class SmartphoneAdminForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         instance = kwargs.get('instance')
#         if not instance.sd:
#             self.fields['sd_volume_max'].widget.attrs.update({
#                 'readonly': True, 'style': 'background: lightgray'
#             })
#
#     def clean(self):
#         if not self.cleaned_data['sd']:
#             self.cleaned_data['sd_volume_max'] = None
#         return self.cleaned_data
#
#
# class SmartphoneAdmin(admin.ModelAdmin):
#     change_form_template = 'admin.html'
#     form = SmartphoneAdminForm
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'category':
#             return ModelChoiceField(Category.objects.filter(slug='Smartphone'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)


class GameBoxAdmin(admin.ModelAdmin):
    readonly_fields = ['status']


# admin.site.register(Category)
# admin.site.register(Notebook, NotebookAdmin)
# admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
# -------------------------------------------
admin.site.register(GameCategory)
admin.site.register(GameBox, GameBoxAdmin)
admin.site.register(Game)
