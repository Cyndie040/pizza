from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HelloOrderView.as_view(), name='hello_order'),
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),  # replace with your actual view name
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_status'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_orders'),  # replace with your actual view name
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetail.as_view(), name='user_order_detail'),  # replace with your actual view name
]
