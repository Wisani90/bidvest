from django.urls import path

from . import views
    
urlpatterns = [
    path('api/doc/profile/', views.ProfileListCreate.as_view() ),
    path('api/doc/billed/', views.BilledListCreate.as_view() ),
    path('api/doc/item/', views.ItemListCreate.as_view() ),
    path('api/doc/user/', views.UserListCreate.as_view() ),
    path('pdf/', views.GeneratePdf.as_view() )
]