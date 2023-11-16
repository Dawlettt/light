from django.urls import path

from .views import device_list, device_detail

urlpatterns = [
    path('device_list/', device_list),
    path('device_list/<int:id>/', device_detail)
]
