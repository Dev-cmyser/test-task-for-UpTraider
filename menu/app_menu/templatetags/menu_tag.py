from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    active_item = context['request'].path
    active_items = []
    

    if active_item:
        active_items.append(active_item)
        item = MenuItem.objects.filter(url=active_item).first()
        while item and item.parent:
            active_items.append(item.parent.url)
            item = item.parent

    def render_menu_items(items):
        result = ''
        for item in items:
            
            # один запрос к бд
            children = MenuItem.objects.filter(parent=item).select_related('parent')

            has_children = children.exists()
            is_active = item.url in active_items

            result += f'<li class="{ "active" if is_active else "" }{ "has-children" if has_children else "" }">'
            result += f'<a class="link" href="{ item.url }">{ item.name }</a>'

            if has_children:
                result += render_menu_items(children)

            result += '</li>'

        return result

    if menu_name is not None:
        menu_items = MenuItem.objects.filter(name=menu_name, parent=None)
    if menu_items:
        result = '<ul class="menu">'
        result += mark_safe(render_menu_items(menu_items))
        
        result += '</ul>'
        return format_html(result)

    return ''




