from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percentage', 'active']
    list_filter = ['active']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
