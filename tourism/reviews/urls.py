
from django.urls import path

from . import views


urlpatterns = [

    path("", views.place_index, name="place_index"),
   
    # path("show_result", views.add_new_data, name="add_new_data"),
    path("add_review", views.add_review, name="add_review"),
    path("<int:pk>/", views.place_detail, name="place_detail"),
    path("real_result", views.get_review, name="get_review"),

]