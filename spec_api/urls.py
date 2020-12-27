from django.urls import path
from . import views
urlpatterns = [
    path('product-list/', views.productList,name="product-list"),
    path('product-detail/<int:pk>', views.productDetail,name="product-detail"),
    path('product-search/', views.productSearchWithoutParam,name="product-search-without-param"),
    path('product-search/<str:searchText>', views.productSearch,name="product-search"),
    path('sslcommerz/', views.sslCommerz, name='ssl-commerz'),
    path('sslcommerz/success/',views.sslcommerzResult, name='sslcommerz-success'),
    path('sslcommerz/fail/',views.sslcommerzfail, name='sslcommerz-fail'),
    path('sslcommerz/cancel/',views.sslcommerzcancel, name='sslcommerz-cancel'),
    path('sslcommerz/tranid/<str:id>',views.sslcomerzTranId, name='sslcommerz-tranid')
]