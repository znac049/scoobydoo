from django.utils import timezone
from django.views.generic import TemplateView, ListView
from .models import Tape


class HomePage(TemplateView):
    template_name = "home.html"

class TapeListView(ListView):
    model = Tape
    #paginate_by = 100
    template_name = "tape_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["now"] = timezone.now()

        return context