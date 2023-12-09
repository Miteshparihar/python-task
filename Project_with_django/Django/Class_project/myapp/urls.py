from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.sign,name='sign'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('verify/',views.verify,name='verify'),
    path('create_password/',views.create_password,name='create_password'),
    path('change_password/',views.change_password,name='change_password'),
    path('farmer_change_pas/',views.farmer_change_pas,name='farmer_change_pas'),
    path('farmer_home/',views.farmer_home,name='farmer_home'),
    path('add_product/',views.add_product,name='add_product'),
    path('our_products/',views.our_products,name='our_products'),
    path('product_detail/<int:pk>',views.product_detail,name='product_detail'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('my_blog/',views.my_blog,name='my_blog'),
    path('shop/',views.shop,name='shop'),
    path('shop_detail/<int:pk>',views.shop_detail,name='shop_detail'),
    path('add_to_wishlist/<int:pk>',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove_wishlist/<int:pk>',views.remove_wishlist,name='remove_wishlist'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('change_qty/<int:pk>',views.change_qty,name='change_qty'),
    path('remove_cart/<int:pk>',views.remove_cart,name='remove_cart'),
    path('customer_show_blog',views.customer_show_blog,name='customer_show_blog'),
    path('farmer_c_dashboard/',views.farmer_c_dashboard,name='farmer_c_dashboard'),
    path('c_dashboard/',views.c_dashboard,name='c_dashboard'),
    path('dash_header/',views.dash_header,name='dash_header' ),
    path('farmer_dash_header/',views.farmer_dash_header,name='farmer_dash_header' ),
    path('c_dash_profile/',views.c_dash_profile,name='c_dash_profile'),
     path('farmer_c_dash_profile/',views.farmer_c_dash_profile,name='farmer_c_dash_profile'),
    path('d_cart/',views.d_cart,name='d_cart'),
    path('rd_cart/<int:pk>',views.rd_cart,name='rd_cart'),
    path('d_wish',views.d_wish,name='d_wish'),
    path('rd_wish/<int:pk>',views.rd_wish,name='rd_wish'),
    path('cart/success',views.success,name='success'),
    path('d_order/',views.d_order,name='d_order'),
    path('farmer_c_my_blog/',views.farmer_c_my_blog,name='farmer_c_my_blog'),
    path('farmer_c_my_product/',views.farmer_c_my_product,name='farmer_c_my_product'),
    path('ajax/ajax_validation/',views.ajax_validation,name='ajax_validation'),
]