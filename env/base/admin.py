from django.contrib import admin

# Register your models here.
# models of admin panel to see super user as well as other users to be added

from . import models as m

admin.site.register(m.Room)
admin.site.register(m.Topic)
admin.site.register(m.Message)