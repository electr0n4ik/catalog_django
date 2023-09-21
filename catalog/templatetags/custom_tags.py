from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.simple_tag
def mediapath(path):
    return '/media/' + str(path)


@register.filter()
def is_moderator(val):
    moderators = Group.objects.get(name="moderators").user_set.all()
    if val in moderators:
        return True
    return False


@register.filter()
def is_content_moderator(val):
    moderators = Group.objects.get(name="content_moderators").user_set.all()
    if val in moderators:
        return True
    return False
