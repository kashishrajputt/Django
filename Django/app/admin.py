from django.contrib import admin
from .models import AppVarity, Review, Store, Certificate

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2

class VarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(AppVarity, VarietyAdmin )
admin.site.register(Store, StoreAdmin)
admin.site.register( Certificate, CertificateAdmin)

