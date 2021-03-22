from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from device import views
from device.views import DeviceListView,  UsersListView, \
    UsersDetailView, UsersUpdateView, CreateUsers, CreateDevice, \
    DeviceUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', DeviceListView.as_view(), name='all_devices'),
    path('users/', UsersListView.as_view(), name='all_users'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='user'),
    path('users/<int:pk>/edit/', UsersUpdateView.as_view(),
         name='edit_user'),
    path('users/new/', CreateUsers.as_view(), name='new_user'),
    path('device/new', CreateDevice.as_view(), name='new_devices'),
    path('device/<int:pk>/edit', DeviceUpdateView.as_view(), name='device'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
