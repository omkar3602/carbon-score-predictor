from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adminuser', RedirectView.as_view(url=reverse_lazy('admin:index')), name='adminuser'),
]