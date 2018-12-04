from django.urls import path

from . import views
    
urlpatterns = [
    path('api/invoicing/invoices/', views.InvoiceListCreate.as_view() ),
    path('api/invoicing/invoice/<int:pk>/', views.InvoiceDetail.as_view() ),

]