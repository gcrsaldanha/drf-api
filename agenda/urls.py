from django.urls import path
from agenda.views import AgendamentoDetail, AgendamentoList, get_horarios, get_relatorio_prestadores, index

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:pk>/', AgendamentoDetail.as_view()),
    path('horarios/', get_horarios),
    path('prestadores/', get_relatorio_prestadores),
    path('', index),
]
