

from family_app.views import add_member,add_relationship,find_shortest_path
from django.urls import path

urlpatterns = [
    path("add-member",add_member , name="add_member"),
    path("add-relation",add_relationship , name="add_relation"),
    path("shortest-path-count",find_shortest_path, name="shortest_path_count")
]
