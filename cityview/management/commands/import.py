from django.core.management.base import NoArgsCommand
from django.core.exceptions import ObjectDoesNotExist
from cityview.models import *
import urllib2
import json

# Command object to load city information from the specified URL.
# python manage.py import
class Command(NoArgsCommand):
    help = "Downloads the sba.gov city information for California into the database."
    data_url = 'http://api.sba.gov/geodata/city_links_for_state_of/CA.json'
    states = State.objects.all()
    counties = County.objects.all()


    def handle(self, *args, **options):
        """
        Loop through the data returned from the configured service and process all records marked as a city.
        :param args:
        :param options:
        """
        json = self.get_json()

        for data_dict in json:
            if data_dict['fips_class'].startswith('C'):
                state = self.add_state(data_dict)
                county = self.add_county(data_dict, state)
                city = self.add_city(data_dict, county)

            print city
            print "\n"

    def get_json(self):
        """"
        Use the configured data_url to load the city JSON
        """
        req = urllib2.Request(self.data_url)
        opener = urllib2.build_opener()
        handle = opener.open(req)

        return json.loads(handle.read())

    def add_city(self, data_dict, county):
        """
        Attempt to add a new city if it does not already exist.
        :param data_dict:
        :param county:
        """
        name = data_dict['name']
        url = data_dict['url']
        lat = data_dict['primary_latitude']
        lon = data_dict['primary_longitude']

        try:
            city = City.objects.get(name=name, county__fips_code=county.fips_code)
        except ObjectDoesNotExist:
            if(lat and lon):
                city = City(name=name, url=url, latitude=lat, longitude=lon, county=county)
                city.save()

        return city

    def add_county(self, data_dict, state):
        """
        Add a county object if it does not exist.
        :param data_dict:
        :param state:
        """
        name = data_dict['county_name']
        if 'county_full_name' in data_dict:
            full_name = data_dict['county_full_name']
        else:
            full_name = ''

        fips_code = data_dict['fips_county_cd']

        try:
            county = self.counties.get(fips_code=fips_code)
        except ObjectDoesNotExist:
            county = County(name=name, full_name=full_name, fips_code=fips_code, state=state)
            county.save()
            counties = County.objects.all()

        return county

    def add_state(self, data_dict):
        """
        Add a state object if it does not exist.
        :param data_dict:
        """
        name = data_dict['state_name']
        abbrev = data_dict['state_abbreviation']

        try:
            state = self.states.get(abbreviation=abbrev)
        except ObjectDoesNotExist:
            state = State(name=name, abbreviation=abbrev)
            state.save()
            self.states = State.objects.all()

        return state

