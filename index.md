# ToC

{% for file in site.static_files %}
{% if file.extname == ".md" and file.basename != "index" %}
[{{ file.basename }}]({{site.baseurl}}/{{file.basename}}.html)
{% endif %}
{% endfor %}

{% for note in site.notes %}
    <a href="{{ note.url }}">{{ note.title }}</a>
{% endfor %}