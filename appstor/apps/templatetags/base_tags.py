from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag("apps/partials/category_nvabar.html")
def category_navbar():
    return {
        "categories": Category.objects.all()
    }