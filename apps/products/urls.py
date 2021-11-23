from django.urls import path
from django.utils.regex_helper import normalize
from apps.products import views

urlpatterns = [
    path('',views.ProductIndexView.as_view(),name='index'),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail'),
]