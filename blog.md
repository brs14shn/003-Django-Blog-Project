# IMAGE FİELD
  1- İnstall # pip install pillow 
  2- <project_name> >> settings.py >> içerisine
  ```
      - import os
      - MEDIA_URL="media/"
     -  MEDIA_ROOT=os.path.join(BASE_DIR, "media")
 ```
   
  3- <project_name> >>urls.py file içerisine 👇
  # View Static/Media Files:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) komut eklenir.


## CRISPY FORMS

go to terminal

```bash
pip install django-crispy-forms
pip freeze > requirements.txt
```

go to settings.py

```python
INSTALLED_APPS = (
    ...
    'crispy_forms',
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#html
<div style="width:300px;">
  {% load crispy_forms_tags %}
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %} {% comment %} {{ form.as_p }} {% endcomment %} {{ form |
    crispy}}
    <input type="submit" value="OK" />
  </form>
</div>