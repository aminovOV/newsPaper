from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from .censor import censor_list


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category',
                  'headline',
                  'body_text',
                  'author', ]

    def clean(self):
        cleaned_data = super().clean()
        headline = cleaned_data.get('headline')
        body_text = cleaned_data.get('body_text')
        for word in headline.split():
            if word in censor_list():
                raise ValidationError(
                    'Заголовок публикации не должен содержать нецензурные выражения.'
                )
        for word in body_text.split():
            if word in censor_list():
                raise ValidationError(
                    'Текст публикации не должен содержать нецензурные выражения.'
                )
        if body_text == headline:
            raise ValidationError(
                'Текст публикации не должен быть идентичен заголовку'
            )
        if headline[0].islower() or body_text[0].islower():
            raise ValidationError(
                'Заголовок и текст публикации должны начинаться с заглавной буквы'
            )
        return cleaned_data
