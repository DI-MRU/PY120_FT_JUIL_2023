from django.urls import path

from .views import *

urlpatterns = [
    path('rent/rental', RentalList.as_view(), name='rental-list'),
    path('rent/rental/<int:pk>', RentalDetail.as_view(), name ='rental-detail')
    
]