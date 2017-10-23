from django.conf.urls import url
from apps.universidad.views import index_univ
urlpatterns = [
url(r'^index$', index_univ)
]