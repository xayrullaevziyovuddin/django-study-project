from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=255, default='default_order_name' , verbose_name='Имя'  )
    order_phone = models.CharField(max_length=255, verbose_name='Телефон')

    def __str__(self):
        return self.order_name


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

'''

python manage.py shell
from crm.models import Order
from django.db import connection

 new_order = Order(order_name='Hiki', order_phone='+9999999999')
new_order.save()

Сразу авт сохранить 
n3 = Order.objects.create(order_name = 'Anna', order_phone = '+9998888888')

Order.objects.all()

Order.objects.filter(order_name = 'Anna')


 Order.objects.order_by('order_name')


 Order.objects.get(pk=3)     
'''