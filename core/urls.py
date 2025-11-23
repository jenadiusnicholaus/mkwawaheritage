from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('heritage/', views.heritage_view, name='heritage'),
    path('heritage/chief/<slug:slug>/', views.chief_detail, name='chief_detail'),
    path('tourism/', views.tourism_view, name='tourism'),
    path('tourism/<slug:slug>/', views.tourism_detail, name='tourism_detail'),
    path('booking/<str:reference>/', views.booking_confirmation, name='booking_confirmation'),
    path('products/', views.products_view, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
