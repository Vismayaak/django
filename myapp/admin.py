from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(usermodel)
admin.site.register(Book)
admin.site.register(employee)
admin.site.register(Product)
class customeradmin(admin.ModelAdmin):
    list_display=('first_name','last_name','address',)
    search_fields=('first_name',)
    list_filter=('first_name',)
admin.site.register(Customer,customeradmin)
admin.site.site_header='MY_SITE'

class blogadmin(admin.ModelAdmin):
    list_display=('title','author','created_at')
    search_fields=('title',)
    list_filter=('author','created_at',)
admin.site.register(blogmodel,blogadmin)
admin.site.site_header="Blog management site"
admin.site.register(user_pro)
admin.site.register(product_use)
admin.site.register(Organizer)
admin.site.register(Event)

admin.site.register(Category)
admin.site.register(Product_cate)

admin.site.register(Hotel)
admin.site.register(Booking)

admin.site.register(user10)
admin.site.register(Post1)
admin.site.register(UserRegistration)

admin.site.register(Image)