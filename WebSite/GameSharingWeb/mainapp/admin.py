from django.contrib import admin
from .models import *


class GameBoxAdmin(admin.ModelAdmin):
    readonly_fields = ['status']


admin.site.register(CartGame)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
# -------------------------------------------
admin.site.register(GameCategory)
admin.site.register(GameBox, GameBoxAdmin)
admin.site.register(Game)
#admin.site.register(BagRoom)
#admin.site.register(Event)
#admin.site.register(Rent)