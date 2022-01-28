from django import template

censor = ['котики', 'подобию', 'стать']
register = template.Library()


@register.filter(name = 'block_words')
def block_words(value):
    text = value.split()
    for word in text:
        if word.lower() in censor:
            value = value.replace(word, '********')
    return value
