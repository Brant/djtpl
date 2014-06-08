---
title: Features
layout: page
---

The purpose of djtpl is to provide a much faster and more robust starting project structure.

It includes the following, preconfigured using settings.py:

- Centralized directory for templates
- Centralize directory for static files (js, css, and images)
- Pre-configured base URL file
- Placement for uploads (MEDIA_ROOT)

See also: [Tools Included]({{ "/tools/" | prepend: site.baseurl }})

## Annotated Directory Structure
<div class="fake-code">
my_project <strong>(base)</strong><br/>
..assets<br/>
....themes<br/>
......my_project<br/>
........static <strong>(css, js, images)</strong><br/> 
........templates <strong>(all site templates belong here)</strong><br/>
....uploads <strong>(MEDIA_ROOT)</strong><br/>
..my_project <strong>(base django app)</strong><br/>
....local_settings.template.py <strong>(rename this to "local_settings.py")</strong><br/>
....settings.py<br/>
....urls.py<br/>
..manage.py<br/>
..requirements.txt<br/>
</div>
