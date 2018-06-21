{% for note in site.notes %}
[{{ note.title }}]({{ site.baseurl }}{{ note.url }})
{% endfor %}