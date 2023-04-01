from django import template
from cards.models import BOXES, Card

register = template.Library()

@register .inclusion_tag("cards/box_links.html")
def box_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(boc=box_num).count()
        boxes.append({
            "number":box_num,
            "card_count": card_count,
        })
    return {"boxes": boxes}