# Generated by Django 4.0.4 on 2022-06-23 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='statusresponse',
            name='user_initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь инициатор'),
        ),
        migrations.AddField(
            model_name='responseorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='responseorder',
            name='response_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='order',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.categoryorder', verbose_name='Категория'),
        ),
    ]
