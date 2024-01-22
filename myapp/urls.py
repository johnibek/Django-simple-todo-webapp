from django.urls import path
from . import views


urlpatterns = [
    # ----------------Home Page----------------
    path('', views.home, name='home'),
    
    # --------------Removing items-------------
    path('del/<str:item_id>', views.remove, name='del'),
]
