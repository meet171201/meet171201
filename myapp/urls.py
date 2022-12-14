from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('user_wishlist<int:pk>/',views.user_wishlist,name='user_wishlist'),
    path('mywishlist/',views.mywishlist,name='mywishlist'),
    path('Remove_To_wishlist/<int:pk>/',views.Remove_To_wishlist,name='Remove_To_wishlist'),
    path('user_cart/<int:pk>/',views.user_cart,name='user_cart'),
    path('mycart/',views.mycart,name='mycart'),
    path('Remove_To_cart/<int:pk>/',views.Remove_To_cart,name='Remove_To_cart'),
    path('change_qty/<int:pk>/',views.change_qty,name='change_qty'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('myorder/',views.myorder,name='myorder')
    
]

