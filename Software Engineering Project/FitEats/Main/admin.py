from django.contrib import admin
from Main.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return True

admin.site.register(CustomUser, CustomUserAdmin)

"""admin.site.register(CustomUser)"""