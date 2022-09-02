
from django.contrib import admin
from .models import Payment
from .models import Order_Master
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("card_no","cvv","expiry","balance")

admin.site.register(Payment,PaymentAdmin)


class Order_MasterAdmin(admin.ModelAdmin):
    list_display = ('id','username','date_of_order','amount','service_details')
    


admin.site.register(Order_Master,Order_MasterAdmin)
