from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from device.models import Device, Users


def home(request):
    return render(request, 'home.html', {'home': home})


class DeviceListView(ListView):
    model = Device
    template_name = 'devices.html'
    slug_field = 'pk'
    context_object_name = 'all_devices'


class UsersListView(ListView):
    model = Users
    template_name = 'users.html'
    slug_field = 'pk'
    context_object_name = 'all_users'



class UsersDetailView(DetailView):
    model = Users
    template_name = 'user.html'
    slug_field = 'pk'
    context_object_name = 'user'


class UsersUpdateView(UpdateView):
    model = Users
    template_name = 'edit_user.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'users'
    fields = ['first_name', 'last_name', 'avatar', 'phone', 'departament']
    success_url = '/'


class CreateUsers(CreateView):
    model = Users
    fields = ['first_name', 'last_name', 'avatar']
    template_name = 'create_user.html'
    success_url = '/users/'


class CreateDevice(CreateView):
    model = Device
    fields = ['device', 'configuration', 'price', 'paid_by', 'used_by',
              'comment', 'start_date']
    template_name = 'create_device.html'
    success_url = '/devices/'


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = 'edit_device.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    context_object_name = 'devices'
    fields = ['device', 'configuration', 'price', 'paid_by', 'used_by',
              'comment', 'start_date']
    success_url = '/devices/'
