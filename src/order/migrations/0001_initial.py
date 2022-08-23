# Generated by Django 4.0.6 on 2022-08-23 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_course_course_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=25, verbose_name='شماره سفارش')),
                ('order_note', models.CharField(blank=True, max_length=150, null=True, verbose_name='توضیحات سفارش')),
                ('order_total', models.FloatField(verbose_name='جمع سفارش')),
                ('status', models.CharField(choices=[('New', 'جدید'), ('Accepted', 'تایید شده'), ('Completed', 'تکمیل شده'), ('Cancelled', 'کنسل شده')], default='New', max_length=15, verbose_name='وضعیت سفارش')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='آی پی کاربر ')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده است  ')),
                ('date_Order', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت ')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment', verbose_name='نوع پرداخت ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='یوزر سفارش دهنده')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارش ها',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.IntegerField(verbose_name='قیمت محصول')),
                ('order_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش محصول')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='دوره مورد نظر')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='سفارش مربوط')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment', verbose_name='نوع پرداخت ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='یوز سفارش دهنده')),
            ],
            options={
                'verbose_name': 'سفارش محصول',
                'verbose_name_plural': 'بخش سفارش محصول',
            },
        ),
    ]
