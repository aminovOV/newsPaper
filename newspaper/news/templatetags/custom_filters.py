from django import template
from ..censor import censor_list


register = template.Library()


@register.filter()
def censor(text):
    for word in text.split():
        if word in censor_list():
            text = text.replace(word, f'{word[0]}{"*"*(len(word)-1)}')
    return text
