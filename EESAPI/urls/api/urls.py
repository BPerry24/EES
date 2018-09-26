from django.urls import path
from EESAPI.views.api.SpillDetail import SpillDetail

# API Urls
app_name = 'api'

urlpatterns = [
    path('spill/detail', SpillDetail.as_view, name='spill_detail'),
]
