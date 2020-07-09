from django import forms
from django.contrib import admin

from .models import Showcode, Comment, Image, Imgcomment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ShowcodeAdminForm(forms.ModelForm):
    MyMapView_text = forms.CharField(label='Текст статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Showcode
        fields = '__all__'


class ShowcodeAdmin(admin.ModelAdmin):
    form = ShowcodeAdminForm

admin.site.register(Showcode, ShowcodeAdmin)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Imgcomment)