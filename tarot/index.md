---
layout: page
title: "오늘의 타로점"
description: "원하시는 카드를 선택해 타로점의 의미를 확인해 보세요."
permalink: /tarot/
---

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 2rem;">
  {% assign cards = site.projects %}
  {% for card in cards %}
    <a href="{{ card.url | relative_url }}" style="text-decoration: none; color: inherit; text-align: center; display: block; padding: 10px; border-radius: 8px; transition: transform 0.2s ease-in-out;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
      <img src="{{ card.image.path | relative_url }}" alt="{{ card.title }}" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
      <h3 style="margin-top: 15px; font-size: 1.2em;">{{ card.title }}</h3>
    </a>
  {% endfor %}
</div>
