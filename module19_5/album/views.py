from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Album
from .forms import AlbumForm
from musician.models import Musician
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')  # Redirect after successful form submission

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # Filter the musician field to show only those related to the logged-in user
        form.fields['musician'].queryset = Musician.objects.filter(author=self.request.user)
        return form


from django.views.generic.edit import UpdateView
@method_decorator(login_required, name='dispatch')

class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'  # Reuse the same template for both add and edit
    success_url = reverse_lazy('homepage')  # Redirect after successful edit
    pk_url_kwarg= 'id'
