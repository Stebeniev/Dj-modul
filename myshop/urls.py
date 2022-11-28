from django.urls import path
from . import views
from myshop.views import ProductView, Logout, Login, Register, ProductCreateView, ProductUpdateView, PurchaseListView, \
    PurchasesCreateView, ReturnCreateView, ReturnListView

# ReturnListView


urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('signup/login/', Login.as_view(), name='login'),
    path('accounts/profile/', views.site, name='site'),
    path('new/product', ProductCreateView.as_view(), name='new_product'),
    path('update/product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('purchase/create/', PurchasesCreateView.as_view(), name='purchase_create'),
    path('purchase/', PurchaseListView.as_view(), name='purchase'),
    path('return/', ReturnCreateView.as_view(), name='return'),
    path('add/return/', ReturnListView.as_view(), name='add_return'),

]