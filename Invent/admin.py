from django.contrib import admin
from .models import*
class productAdmin(admin.ModelAdmin):
    list_display = ('product_name','room_no')
class ProductMessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp')
# Register your models here.
admin.site.register(Cate)
admin.site.register(Room)
admin.site.register(Product,productAdmin)
admin.site.register(ProductMessage,ProductMessageAdmin)







