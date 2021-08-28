from django.urls import path
from .views import(
    ProductCreateView,
    Product_list
)

urlpatterns = [

    path('p/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('', Product_list.as_view(), name='Product_list'),

]
