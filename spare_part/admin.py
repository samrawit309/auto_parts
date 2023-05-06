from django.contrib import admin
from spare_part.models import Make
from spare_part.models import ModelCar
from spare_part.models import Entry
admin.site.register(Make)
admin.site.register(ModelCar)
admin.site.register(Entry)

# Register your models here.
