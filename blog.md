# IMAGE FİELD
  1- İnstall # pip install pillow 
  2- <project_name> >> settings.py >> içerisine
      - import os
      - MEDIA_URL="media/"
     -  MEDIA_ROOT=os.path.join(BASE_DIR, "media")
   
  3- <project_name> >>urls.py file içerisine 👇
  # View Static/Media Files:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) komut eklenir.