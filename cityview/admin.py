from django.contrib import admin
from cityview.models import *

class CityAdmin(admin.ModelAdmin):
    """
    An admin model to configure the city administration list page.
    """
    list_display = ('name', 'county', 'state', 'latitude','longitude')
    # Allow the user to filter by county.
    list_filter = ['county']

    def state(self, city):
        """
        This returns the field used to filter/list within the admin.
        :param city:
        """
        return city.county.state.name
    state.admin_order_field = 'city__state'

    def county(self, city):
        """
        This returns the field used to filter/list the county within the admin.
        :param city:
        """
        return city.county.name
    county.admin_order_field = 'city__county'

admin.site.register(State)
admin.site.register(County)
admin.site.register(City, CityAdmin)
