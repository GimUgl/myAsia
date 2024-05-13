from django import template

from myAsia_blog.models import Genres


register = template.Library()

@register.simple_tag()
def get_genres():
    genres = Genres.objects.all()
    return genres
