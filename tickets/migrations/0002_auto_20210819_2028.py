# Generated by Django 3.2.4 on 2021-08-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='due',
            field=models.DateField(null=True),
        ),
    ]
