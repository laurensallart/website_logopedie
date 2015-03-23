from django.contrib import admin
from oefening.models import *
from django.contrib import admin


# Add in this class to customized the Admin Interface
class ChildAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('userName',)}

class OpgaveAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class reeksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Update the registeration to include this customised interface
admin.site.register(Child, ChildAdmin)
admin.site.register(Opgave, OpgaveAdmin)
admin.site.register(Oefeningenreeks, reeksAdmin)
admin.site.register(Resultaat)
admin.site.register(UserProfile)
admin.site.register(Answer)


# Register your models here.
