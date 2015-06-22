__author__ = 'tumivn'

from MovieLib.models import Movie

class MovieMixin(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs
