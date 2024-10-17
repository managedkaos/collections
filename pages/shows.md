---
layout: page
title: Shows
permalink: "/shows/"
---



<ul>
{% for item in site.shows %}
    <li>
        <a href="{{ item.url | prepend: site.baseurl }}"> {{ item.title }} </a>
        <p class="post-excerpt">{{ item.status }}</p>
        <p class="post-excerpt">{{ item.description }}</p>
    </li>
{% endfor %}
</ul>
