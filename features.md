---
title: Features
layout: page
---

The purpose of djtpl is to provide a much faster and more robust starting project structure.

It includes the following, preconfigured using settings.py:

- Centralized directory for templates
- Centralize directory for static files (js, css, and images)
- Pre-configured base URL file
- Placement for uploads (corresponds to MEDIA_ROOT)

See also: [Tools Included]({{ "/tools/" | prepend: site.baseurl }})

## Annotated Directory Structure
<div class="fake-code">
my_project (base)<br/>
..assets<br/>
....themes<br/>
......my_project<br/>
........static (css, js, images)<br/> 
........templates (all site templates belong here)<br/>
....uploads (MEDIA_ROOT)<br/>
..my_project (base django app)<br/>
....local_settings.template.py (rename this to "local_settings.py")<br/>
....settings.py<br/>
....urls.py<br/>
..manage.py<br/>
..requirements.txt<br/>
</div>
