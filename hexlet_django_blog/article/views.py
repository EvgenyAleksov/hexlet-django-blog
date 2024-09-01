from django.http import HttpResponse
from django.views import View

class HomePageView(View):

    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

