# Create your views here.
from django.views import generic
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from cityview.models import City, County


class IndexView(generic.ListView):
    model = City
    template_name = 'cityview/index.html'
    context_object_name = 'cities'
    paginate_by = 25

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if 'county_id' in self.kwargs:
            county = get_object_or_404(County, id=self.kwargs['county_id'])
            cities = City.objects.filter(county=county)
        else:
            cities = City.objects.all()

        return cities

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if 'county_id' in self.kwargs:
            context['county'] = get_object_or_404(County, id=self.kwargs['county_id'])

        return context

