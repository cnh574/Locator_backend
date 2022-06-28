from django.urls import path
from . import views

urlpatterns = [
    path('api/locator', views.LocatorList.as_view(), name='locator_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/locator/<int:pk>', views.LocatorDetail.as_view(), name='locator_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
