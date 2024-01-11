from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, Http404
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, ArchiveIndexView, MonthArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from .forms import BbForm
from .models import Bb, Rubric


# def index(request):
#     bbs = Bb.objects.all()
#     rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
#     context = {'bbs': bbs, 'rubrics': rubrics}
#     return HttpResponse(
#         render_to_string('index.html', context, request)
#     )
class BbIndexView(ArchiveIndexView):
    model = Bb
    template_name = 'index.html'
    date_field = 'published'
    date_list_period = 'year'
    context_object_name = 'bbs'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbMonthView(MonthArchiveView):
    model = Bb
    template_name = 'index.html'
    date_field = 'published'
    date_list_period = 'month'
    month_format = '%m'
    context_object_name = 'bbs'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbRedirectView(RedirectView):
    url = '/'


# def by_rubric(request, rubric_id):
#     bbs = Bb.objects.filter(rubric=rubric_id)
#     rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
#     current_rubric = Rubric.objects.get(pk=rubric_id)
#     context = {'bbs': bbs, 'rubrics': rubrics,
#                'current_rubric': current_rubric}
#     return render(request, 'by_rubric.html', context)


class BbByRubricView(ListView):
    template_name = 'by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context
# class BbByRubricView(TemplateView):
#     template_name = 'by_rubric.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
#         return context


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

# def add_and_save(request):
#     print(request.headers['Accept-Encoding'])
#     print(request.headers['accept-encoding'])
#     print(request.headers['accept_encoding'])
#     print(request.headers['Cookie'])
#     print(request.resolver_match)
#     print(request.body)
#
#     if request.method == 'POST':
#         bbf = BbForm(request.POST)
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(
#                 reverse('bboard:by_rubric',
#                         kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk})
#             )
#         else:
#             context = {'form': bbf}
#             return render(request, 'create.html', context)
#     else:
#         bbf = BbForm()
#         context = {'form': bbf}
#         return render(request, 'create.html', context)


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context

#homework19
class AllUsersView(View):
    template_name = 'all_users.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})

class UserDetailsView(View):
    template_name = 'user_details.html'

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        return render(request, self.template_name, {'user': user, 'current_user': request.user})

# class BbAddView(FormView):
#     template_name = 'create.html'
#     form_class = BbForm
#     initial = {'price' : 0.0}
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         return context
#
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_form(self, form_class=None ):
#         self.object = super().get_form(form_class)
#         return self.object
#
#     def get_success_url(self):
#         return reverse('bboard:by_rubric', kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})

#crud
class BbCreateView2(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context