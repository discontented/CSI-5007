# ToC
{% include_relative _includes/mathjax.html %}

{% for file in site.static_files %}
{% if file.extname == ".md" and file.basename != "index" %}
[{{ file.basename }}]({{site.baseurl}}/{{file.basename}}.html)
{% endif %}
{% endfor %}