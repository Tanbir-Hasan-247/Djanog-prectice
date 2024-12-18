from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_album')  # Redirect after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)


from django.views.generic.edit import UpdateView
@method_decorator(login_required, name='dispatch')

class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_album')  # Redirect after successful edit
    pk_url_kwarg= 'id'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure author remains the logged-in user
        return super().form_valid(form)


from django.views.generic.edit import DeleteView
@method_decorator(login_required, name='dispatch')

class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'userpost.html'  # Template to confirm deletion
    success_url = reverse_lazy('homepage')  # Redirect after successful deletion
    pk_url_kwarg= 'id'
