from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from hierarchy_app.models import Pokemon

# Register your models here.
admin.site.register(Pokemon, DraggableMPTTAdmin)