"""
URL configuration for Gideon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views
from store import mpesa
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.products,name='products'),
    path('product/<int:products_id>/',views.product_detail,name='productsdetail'),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("profile/",views.profile,name='profile'),
    path('login',views.login_view,name='login'),
    path("signup/", views.signup_view, name='signup'),
    path('addcart/<int:products_id>/',views.add_to_cart,name='addcart'),
    path("remove-from-cart/<int:pk>/", views.remove_from_cart, name='remove_from_cart'),
    path('viewcart',views.cart_view,name='viewcart'),
    path('stkpush/', mpesa.lipa_na_mpesa_online, name='stkpush'),
    path('stk_callback/', mpesa.stk_callback, name='stk_callback'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
