from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


# Create your views here.


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('<h1>This is from class based view</h1>')


class HelloWorldTemlateView(TemplateView):
    template_name = 'testapp/result.html'


class HelloWorldTemplateContext(TemplateView):
    template_name = 'testapp/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Samir'
        context['subject'] = 'Python'
        context['marks'] = 100
        return context
