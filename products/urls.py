from django.urls import path
from .views import(
    ProductCreateView,
    Product_list,
    PostDetailView,
    UserProductList,
)

urlpatterns = [
    path('user/<str:username>', UserProductList.as_view(), name='user-posts'),

    path('p/<int:pk>/', PostDetailView.as_view(), name='product-detail'),

    path('p/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('', Product_list.as_view(), name='Product_list'),

]
