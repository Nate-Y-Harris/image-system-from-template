from __future__ import annotations
from django.db.models import Q


def apply_keyword_search(queryset, keyword: str):
    final_cardset = queryset.filter(Q(tags__icontains=keyword) | Q(summary__icontains=keyword) | Q(description__icontains=keyword) | Q(title__icontains=keyword))  
    # Tags
    return final_cardset
