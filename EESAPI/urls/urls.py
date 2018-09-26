from django.urls import path, include
from EESAPI.views.index import index

# View Urls
app_name = 'EESAPI'

urlpatterns = [
    path('api/', include('EESAPI.urls.api.urls')),
    path('index/', index, name='index')
]
