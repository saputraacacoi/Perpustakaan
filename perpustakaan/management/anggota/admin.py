from django.contrib import admin
from orm.models import Anggota 

class AngggotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Anggota, AngggotaAdmin)
