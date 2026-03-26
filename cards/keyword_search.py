from __future__ import annotations


def apply_keyword_search(queryset, keyword: str):
    final_cardset = []
    # Tags
    for card in queryset:
        if keyword in card.tags:
            final_cardset.append(card)
            break
        if keyword in card.summary:
            final_cardset.append(card)
            break
        if keyword in card.description:
            final_cardset.append(card)
            break
        if keyword in card.title:
            final_cardset.append(card)
            break
    return final_cardset
