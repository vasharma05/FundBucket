# Generated by Django 3.0 on 2020-02-01 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20200201_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('roll_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(default='https://drive.google.com/open?id=16ZU24pGnhv3UUrdbb6vQSagFGiKHLMWX', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
    ]
