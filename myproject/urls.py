"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my',views.fun2),
    path('new',views.fun3),
    path("fun4",views.fun4),
    path("fun5",views.fun5),
    path("fun6",views.fun6),
    path("fun7",views.fun7),
    path("fun8",views.fun8),
    path("fun9",views.fun9),
    path("fun10",views.fun10),
    path("fun11",views.fun11),
    path("fun12",views.fun12,name='v'),
    path('fun13',views.fun13),
    path('fun14',views.fun14,name='product_table'),
    path('fundelete_user/<int:id>',views.fundelete_user,name='hi'),
    path('update_employee/<int:id>',views.update_user,name='update'),
    path('add',views.cus_add,name='add_customer'),
    path('display',views.cus_display,name='display_customer'),
    path('update/<int:id>',views.cus_update,name='update_customer'),
    path('delete/<int:id>',views.cus_delete,name='delete_customer'),
    path('blogmodel',views.blogcreate,name='create_blog'),
    path('redirectblog',views.blog,name='blog'),
    path('get',views.get_user),


    path('add_organizer',views.add_organizer),
    path('add_event',views.add_event),
    path('display_organizer',views.display_organizer,name='display_organizer'),
    path('display_event',views.display_event,name='display_event'),
    path('update_organizer/<int:id>',views.update_organizer,name='update_organizer'),
    path('update_event/<int:id>',views.update_event,name='update_event'),
    path('delete_organizer/<int:id>',views.delete_organizer,name='delete_organizer'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),

    path('add_product_cate',views.add_product_cate),
    path('display_product_cate',views.display_product_cate,name='display_product_cate'),
    path('update_product_cate/<int:id>',views.update_product_cate,name='update_product_cate'),
    path('delete_product_cate/<int:id>',views.delete_product_cate,name='delete_product_cate'),
    path('hotel_display',views.hotel_display),
    path('booking_display/<int:id>',views.booking_display,name='bookings'),
    path('update_booking/<int:id>',views.update_booking,name='update_bkng'),
    path('delete_booking/<int:id>',views.delete_booking,name='delete_bkng'),
    path('rating_3',views.rating_3,name='rtng_3'),
    path('hi',views.user1),
    path('u_profile',views.u_profile),
    path('profile_view',views.profile_view,name='profileView'),
    path('profile_delete/<int:id>',views.profile_delete,name='profileDelete'),
    path('lh',views.hm),
    path('post_form',views.post_form),
    path('post_view',views.post_view,name='postview'),
    path('postupdate/<int:id>',views.post_update,name='postupdate'),
    path('postdelete/<int:id>',views.post_delete,name='postdelete'),
    path('userform',views.add_userRegistration),
    path('add_user',views.add_userRegistration),
    path('add_img',views.add_image),
    path('view_img',views.view_image),
    path('product_base',views.product_base),
    path('product_product',views.product_product),
    ]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 