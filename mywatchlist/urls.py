from django.urls import path
from mywatchlist.views import show_mywatchlist, show_mywatchlist_json, show_mywatchlist_json_id, show_mywatchlist_xml, show_mywatchlist_xml_id

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('xml/<int:id>', show_mywatchlist_xml_id, name='show_mywatchlist_xml_id'),
    path('json/<int:id>', show_mywatchlist_json_id, name='show_mywatchlist_json_id'),
]