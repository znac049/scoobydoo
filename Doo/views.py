from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from http import HTTPStatus

from .models import Tape, MediaType, StorageLocation


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
    filter_media_type = None
    filter_location = None

    def dispatch(self, request, *args, **kwargs):
        resp = super().dispatch(request, *args, **kwargs)
        if request.method == 'GET':
            self.filter_media_type = request.GET.get('media')
            self.filter_location = request.GET.get('loc')

        print(f"media={self.filter_media_type}, loc={self.filter_location}")
        return resp

    def post(self, request, *args, **kwargs):
        # some project logic
        return JsonResponse({
            'status': HTTPStatus.OK,
            'data': {}
        })

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        print(f"media={self.filter_media_type}, loc={self.filter_location}")
        if self.filter_media_type:
            print(f"Filter by media: '{self.filter_media_type}")
        if self.filter_location != None:
            print(f"Filter by location: '{self.filter_location}")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()

        # Grab data for the filter bar
        context["media_list"] = MediaType.objects.all()
        context["locations_list"] = StorageLocation.objects.all()

        return context