from django.urls import path
from .views import RecordListView, RecordDetailView

urlpatterns = [
    path('records/', RecordListView.as_view(), name='record_list'),
    path('records/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
]
