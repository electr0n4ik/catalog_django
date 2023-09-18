from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet

from catalog.models import Blog, Product, ProductVersion


def forbidden_words_detect(text):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    for forbidden_word in forbidden_words:
        if text in forbidden_words:

            raise forms.ValidationError(f'Недопустимое слово \'{forbidden_word}\'')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'content', 'preview', 'is_published', 'view_count')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        forbidden_words_detect(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words_detect(cleaned_data)
        return cleaned_data


class ProductVersionForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
