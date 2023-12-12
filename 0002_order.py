# Generated by Django 3.1.7 on 2021-07-16 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PizzaDelivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=4)),
                ('price', models.FloatField(max_length=5)),
                ('discount', models.IntegerField(max_length=3)),
                ('total_price', models.FloatField(max_length=5)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PizzaDelivery.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]