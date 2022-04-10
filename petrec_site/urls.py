from django.conf import settings
from django.urls import path
from .views import graph, data, index, feedback, thanks
from django.conf.urls.static import static

app_name = "petrec_site"

urlpatterns = [
    path('home', index, name="index"),
    path('graph/', graph, name="graph"),
    path('data/', data, name="data"),
    path('feedback/', feedback, name="feedback"),
    path('thanks/', thanks, name="thanks"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)