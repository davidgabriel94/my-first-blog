from django.conf.urls import url,include
from apps.alumnos.views import alumno_list

urlpatterns = [
    url(r'^$',alumno_list),
]
