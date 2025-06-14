import json

from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from http import HTTPStatus

from .models import Tape, MediaType, StorageLocation, Movement
from .helpers.viewhelper import ViewHelper

class TapeViewHelper(ViewHelper):
    def __init__(self):
        self.menu = [
            {'label': 'List Tapes', 'url': '/tapes/'},
            {'label': 'Add Tape', 'url': '/tapes/add/'},
            {'label': 'List Tape Movements', 'url': '/movement/'},
            {'label': 'Move Tape(s)', 'url': '/movement/add/'},
        ]


class HomePage(TemplateView):
    template_name = "home.html"

class CreateMovementView(CreateView):
    model = Movement
    fields = ['movement_date', 'tapes', 'location', 'comment']

    def post(self, request, *args, **kwargs):
        # print(self.get_form()['tapes'])
        # print(self.get_form().get_context())

        rst = super().post(request, *args, **kwargs)

        # print(vars(self.object))
        return rst

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()
        context["action"] = "New movement"
        return context


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

class ListMovementView(ListView, ViewHelper):
    model = Movement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()

        return context

class TapeListView(ListView, ViewHelper):
    model = Tape
    #paginate_by = 100
    filter_media_type = None
    filter_location = None

    # POST will only be used by the view to implement live filtering via Ajax
    def post(self, request, *args, **kwargs):
        payload = json.loads(list(request.POST.keys())[0])
        print(json.dumps(payload, indent=2))

        self.filter_media_type = payload['media_type']
        self.filter_location = payload['location']

        self.object_list = self.get_queryset()

        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)

    def get_queryset(self, **kwargs):
        print("get_queryset(...)")

        qs = super().get_queryset(**kwargs)
        print(f"media={self.filter_media_type}, loc={self.filter_location}")

        # Deal with any filtering
        if self.filter_media_type:
            print("filter on media_type")
            rqs = self.model.objects.none()

            for id in self.filter_media_type:
                rqs = rqs | qs.filter(media_type=id)

            qs = rqs.distinct()

        if self.filter_location:
            print("Filter on location")
            rqs = self.model.objects.none()

            for id in self.filter_location:
                rqs = rqs | qs.filter(location=id)

            qs = rqs.distinct()

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()

        # Grab data for the filter bar
        context["media_list"] = MediaType.objects.all()
        context["locations_list"] = StorageLocation.objects.all()

        return context

    def get_template_names(self):
        names = super().get_template_names()
        if self.is_ajax(self.request):
            print("AJAX!")
            new_names = []
            for name in names:
                print(f"process '{name}'")
                if name.endswith(".html"):
                    name = name.removesuffix(".html") + "_ajax.html"
                new_names += [name]

            names = new_names

        print(f"-> {names}")
        return names