# Generated by Django 2.2.4 on 2020-12-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanjha_admin', '0011_covid_state_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid_state_link',
            name='usa_state',
            field=models.CharField(max_length=200),
        ),
    ]
