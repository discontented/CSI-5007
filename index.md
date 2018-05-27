# ToC

{% for file in site.static_files %}
{% if file.extname == ".md" and file.basename != "index" %}
[{{ file.basename }}]({{site.baseurl}}/{{file.basename}}.html)
{% endif %}
{% endfor %}

{% for note in site.notes %}
[{{ note.basename }}]({{site.baseurl}}/{{note.basename}}.html)
{% endfor %}