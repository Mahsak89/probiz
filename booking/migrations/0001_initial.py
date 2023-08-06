# Generated by Django 3.2.20 on 2023-08-05 22:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Business Strategy Development', 'Business Strategy Development'), ('Financial Planning and Analysis', 'Financial Planning and Analysis'), ('Market Research and Analysis', 'Market Research and Analysis'), ('Process Optimization', 'Process Optimization'), ('Leadership Development', 'Leadership Development'), ('Change Management', 'Change Management'), ('consulting', 'consulting')], default='Business Strategy Development', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM')], default='3 PM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]