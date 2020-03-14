from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.

class topView(TemplateView):
	template_name = "top.html"

	def get(self, request, *args, **kwargs):
		context = super(topView, self).get_context_data(**kwargs)
		return render(self.request, self.template_name, context)