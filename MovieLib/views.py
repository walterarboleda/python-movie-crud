from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from MovieLib.forms import MovieMixin
from MovieLib.models import Movie

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Movie

class CreateView(CreateView):
    template_name = 'create.html'
    model = Movie
    success_url = '/'

class UpdateView(UpdateView):
    template_name = 'update.html'
    model = Movie
    success_url = '/'

class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    def get_success_url(self):
        return reverse('movie_index')