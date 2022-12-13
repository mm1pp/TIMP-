from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/<slug:slug>/' , views.product_detail, name='product_detail'),
    path('<slug:category_slug>/' , views.category_slug, name='category_slug'),
] 