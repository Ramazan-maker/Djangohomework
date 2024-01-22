from django.shortcuts import render
from django.views import View
from .models import Record

class RecordListView(View):
    template_name = 'record_list.html'

    def get(self, request):
        records = Record.objects.all()
        return render(request, self.template_name, {'records': records})

class RecordDetailView(View):
    template_name = 'record_detail.html'

    def get(self, request, pk):
        record = Record.objects.get(pk=pk)
        return render(request, self.template_name, {'record': record})
