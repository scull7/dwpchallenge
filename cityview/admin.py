from django.contrib import admin
from cityview.models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'county', 'state', 'latitude','longitude')
    list_filter = ['county']

    def state(self, city):
        return city.county.state.name
    state.admin_order_field = 'city__state'

    def county(self, city):
        return city.county.name
    county.admin_order_field = 'city__county'

admin.site.register(State)
admin.site.register(County)
admin.site.register(City, CityAdmin)
