from django import template   # 15

register = template.Library()


def tags(note_tags):
    return ', '.join([str(name) for name in note_tags.all()])


register.filter('tags', tags)
