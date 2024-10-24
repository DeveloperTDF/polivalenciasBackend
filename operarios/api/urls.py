from django.urls import path
from operarios.api.views import OperarioList, OperarioDetail

urlpatterns =   [
    path('', OperarioList.as_view(), name='list'),
    path('<int:pk>', OperarioDetail.as_view(), name='Detail'),
]
