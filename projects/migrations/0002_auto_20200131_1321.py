# Generated by Django 3.0 on 2020-01-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
