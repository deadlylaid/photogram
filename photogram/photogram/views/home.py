from django.generic.view import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"
