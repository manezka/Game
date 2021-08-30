from django import template

register = template.Library()

abnormal_words = ["слово1", "слово2", "слово3", "слово4", "слово5",]


@register.filter(name='censor')
def censor(value):
    words_list = value.split()
    for index, word in enumerate(words_list):
        if word.lower() in abnormal_words:
            words_list[index] = "<...>"
    return "".join(words_list)
