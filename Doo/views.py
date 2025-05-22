from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tape


class ViewHelper():
    menu = []

    def get_side_menu(self):
        return self.menu

class TapeViewHelper(ViewHelper):
    def __init__(self):
        self.menu = [
            {'label': 'List Tapes', 'url': '/tapes/'},
            {'label': 'Add Tape', 'url': '/tapes/add/'},
        ]


class HomePage(TemplateView):
    template_name = "home.html"


class TapeCreateView(CreateView):
    model = Tape
    fields = ['label', 'media_type', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()
        context["action"] = "New Tape"
        return context
 

class TapeUpdateView(UpdateView):
    model = Tape
    fields = ['label', 'media_type', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()
        context["action"] = "Editing Tape"
        return context

class TapeDeleteView(DeleteView):
    model = Tape
    success_url = reverse_lazy('tape-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()
        return context

class TapeListView(ListView, ViewHelper):
    model = Tape
    #paginate_by = 100
    template_name = "tape_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()
        return context