from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric
from django.template import loader


def index(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               "current_rubric": current_rubric}
    return render(request, 'by_rubric.html', context)

def bb_range(request, start_id, end_id):
    bbs = Bb.objects.filter(id__range=[start_id, end_id])
    return render(request, 'template/index.html', {'bbs': bbs, 'title': 'Объявления в диапазоне ID'})

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context