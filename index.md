<!-- {% for note in site.notes %}
    <a href="{{ note.url }}">{{ note.title }}</a>
{% endfor %} -->

{% for note in site.notes %}
[{{ site.baseurl }}{{ note.title }}]({{ note.url }})
{% endfor %}