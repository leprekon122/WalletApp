from django.contrib import admin
from .models import PreTag, WalletTag, WalletData

# Register your models here.
admin.site.register(PreTag)
admin.site.register(WalletTag)
admin.site.register(WalletData)
