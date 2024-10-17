---
layout: page
title: Movies
permalink: "/movies/"
---

<ul>
{% for item in site.movies %}
    <li>
        <a href="{{ item.url | prepend: site.baseurl }}"> {{ item.title }} </a>
        <p class="post-excerpt">{{ item.status }}</p>
        <p class="post-excerpt">{{ item.description }}</p>
    </li>
{% endfor %}
</ul>
