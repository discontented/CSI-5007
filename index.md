{% for note in site.notes %}
    <a href="{{ note.url }}">{{ note.title }}</a>
{% endfor %}