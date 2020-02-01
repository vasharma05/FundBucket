# Generated by Django 3.0 on 2020-02-01 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_auto_20200201_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='department',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='account_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='bank_ifsc',
            field=models.CharField(blank=True, max_length=30, verbose_name='Bank IFSC Code'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
