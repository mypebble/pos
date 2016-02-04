from django.shortcuts import render
from django.views.generic.base import TemplateView


class PosView(TemplateView):
    template_name = 'core/pos.html'
