# Generated by Django 3.2.9 on 2021-11-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
