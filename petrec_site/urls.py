from django.conf import settings
from django.urls import path
from .views import graph, data, index
from django.conf.urls.static import static

app_name = "petrec_site"

urlpatterns = [
    path('home', index, name="index"),
    path('graph/', graph, name="graph"),
    path('data/', data, name="data"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)