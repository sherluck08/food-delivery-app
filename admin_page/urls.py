from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="admin_page-homepage"),
    path("add-to-menu/", views.add_to_menu, name="admin_page-add-to-menu"),
    path("menu/", views.menus, name="admin_page-menus"),
    path("orders/", views.get_orders, name="admin_page-orders"),
    path("menu/<int:menu_id>", views.menu, name="admin_page-menu"),
    path("menu/delete/<int:menu_id>", views.delete_menu, name="admin_page-delete-menu"),
    path("menu/update/<int:menu_id>", views.update_menu, name="admin_page-update-menu"),
]
