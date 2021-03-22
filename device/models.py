from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, default='+375XXXXXXXXX')
    departament = models.CharField(max_length=20, default='name of dep.')
    avatar = models.ImageField(blank=True, default='koa.jpg')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Device(models.Model):
    device = models.CharField(max_length=100)
    configuration = models.CharField(max_length=300)
    price = models.CharField(max_length=5)
    paid_by = models.CharField(max_length=100, blank=True)
    used_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING, blank=True)
    comment = models.CharField(max_length=300, blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.device