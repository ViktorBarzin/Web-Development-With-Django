from django import template
import markdown as mdown # markdown is the Library


register = template.Library()

@register.filter
def markdown(content):
    return mdown.markdown(content)

@register.filter
def tags(tags):
    res = '#' if len(tags) > 0 else ''
    res += res.join(x.name for x in tags)
    return res


