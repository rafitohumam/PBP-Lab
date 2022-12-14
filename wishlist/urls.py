from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_ajax
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_id_json
from wishlist.views import show_id_xml
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_id_json, name='show_id_json'),
    path('xml/<int:id>', show_id_xml, name='show_id_xml'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
