# Generated by Django 2.2.4 on 2021-05-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanjha_admin', '0012_auto_20201221_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
    ]
