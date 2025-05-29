import json

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

    def is_ajax(self, request):
       return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 

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
    filter_media_type = None
    filter_location = None

    def setup(self, request, *args, **kwargs):
        print("setup(...)")
        super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        print("dispatch(...)")
        resp = super().dispatch(request, *args, **kwargs)
        print(request.method)
    
        return resp

    def get(self, request, *args, **kwargs):
        print("get(...)")

        return super().get(request, *args, **kwargs)

    # POST will only be used by the view to implement live filtering via Ajax
    def post(self, request, *args, **kwargs):
        print("post(...)")
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
        if self.filter_media_type:
            print(f"Filter by media: {self.filter_media_type}")
            #qs = qs.filter(media_type_id=self.filter_media_type)
        if self.filter_location != None:
            print(f"Filter by location: {self.filter_location}")
            #qs = qs.filter(location_id=self.filter_location)
        return qs

    def get_context_data(self, **kwargs):
        print("get_content_data()")

        context = super().get_context_data(**kwargs)
        context["side_menu"] = TapeViewHelper().get_side_menu()

        # Grab data for the filter bar
        context["media_list"] = MediaType.objects.all()
        context["locations_list"] = StorageLocation.objects.all()

        return context

    def get_template_names(self):
        print("get_template_names()")

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
        else:
            print("not AJAX")
        print(f"-> {names}")
        return names