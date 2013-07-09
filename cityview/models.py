from django.db import models


# Create your models here.
class State(models.Model):
    abbreviation = models.CharField('Abbreviation', max_length=2)
    name = models.CharField('Name', max_length=30)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.abbreviation)


class County(models.Model):
    name = models.CharField('Name', max_length=100)
    full_name = models.CharField('Full Name', max_length=150)
    fips_code = models.PositiveIntegerField('FIPS Code')
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField('Name', max_length=100)
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    url = models.URLField('City URL')
    county = models.ForeignKey(County)

    def __unicode__(self):
        return self.name

