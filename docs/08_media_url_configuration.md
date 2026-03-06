# Media URL Configuration in Django

This project stores uploaded images such as student face photos and classroom images.

In Django, uploaded files are stored inside the MEDIA_ROOT directory.

Example folder:

    media/
        student_faces/
        classroom_images/

To allow the browser to access these files during development, Django must map MEDIA_URL to MEDIA_ROOT.

Code used:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

This tells Django:

When a request starts with `/media/`, serve files from the `media` folder.

Example:

URL:
    http://127.0.0.1:8000/media/student_faces/img1.jpg

Actual file location:
    project/media/student_faces/img1.jpg