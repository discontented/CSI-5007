<!-- {% for note in site.notes %}
    <a href="{{ note.url }}">{{ note.title }}</a>
{% endfor %} -->

{% for note in site.notes %}
[{{ note.title }}]({{ site.baseurl }}{{ note.url }})
{% endfor %}