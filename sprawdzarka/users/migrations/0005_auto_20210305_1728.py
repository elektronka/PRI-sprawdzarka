# Generated by Django 3.1.7 on 2021-03-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210302_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group_id',
            field=models.CharField(default='0', max_length=100, verbose_name='Grupa'),
        ),
    ]
